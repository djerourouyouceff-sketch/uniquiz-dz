from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.db import transaction
from django.db.models import Avg, Count
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import Course, Quiz, Question, AnswerOption, Attempt, Response
from .forms import SignUpForm

def home(request):
    return render(request, "quiz/home.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = SignUpForm()
    return render(request, "quiz/signup.html", {"form": form})

@login_required
def dashboard(request):
    courses = Course.objects.filter(teacher=request.user) if request.user.is_staff else Course.objects.filter(students=request.user)
    quizzes = Quiz.objects.filter(course__in=courses).select_related("course")
    attempts = Attempt.objects.filter(quiz__course__in=courses, submitted_at__isnull=False).select_related("student", "quiz")
    return render(request, "quiz/dashboard.html", {"courses": courses, "quizzes": quizzes, "attempts": attempts[:30]})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id, is_published=True)
    if not request.user.is_staff and not quiz.course.students.filter(pk=request.user.pk).exists():
        messages.error(request, "You are not enrolled in this course.")
        return redirect("dashboard")
    if Attempt.objects.filter(quiz=quiz, student=request.user, submitted_at__isnull=True).exists():
        return redirect("take_quiz", quiz_id=quiz.id)
    if Attempt.objects.filter(quiz=quiz, student=request.user, submitted_at__isnull=False).exists():
        messages.info(request, "You have already submitted this quiz.")
        return redirect("dashboard")
    if request.method == "POST":
        Attempt.objects.create(quiz=quiz, student=request.user)
        return redirect("take_quiz", quiz_id=quiz.id)
    return render(request, "quiz/quiz_detail.html", {"quiz": quiz})

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id, is_published=True)
    attempt = get_object_or_404(Attempt, quiz=quiz, student=request.user, submitted_at__isnull=True)
    questions = quiz.questions.prefetch_related("options").order_by("order", "id")
    if request.method == "POST":
        with transaction.atomic():
            total = sum((q.points for q in questions), start=0)
            earned = 0
            for question in questions:
                option_id = request.POST.get(f"question_{question.id}")
                option = question.options.filter(pk=option_id).first() if option_id else None
                Response.objects.update_or_create(attempt=attempt, question=question,
                    defaults={"selected_option": option})
                if option and option.is_correct:
                    earned += question.points
            attempt.score = earned
            attempt.max_score = total
            attempt.submitted_at = timezone.now()
            attempt.save()
            if quiz.course.teacher.email:
                send_mail(
                    subject=f"Quiz submitted: {quiz.title}",
                    message=(f"Student: {request.user.get_full_name() or request.user.username}\n"
                             f"Quiz: {quiz.title}\nScore: {earned}/{total}\n"
                             f"Teacher dashboard: please sign in to view detailed results."),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[quiz.course.teacher.email],
                    fail_silently=True,
                )
        return redirect("result", token=attempt.public_token)
    return render(request, "quiz/take_quiz.html", {"quiz": quiz, "questions": questions})

@login_required
def result(request, token):
    attempt = get_object_or_404(Attempt.objects.select_related("quiz", "student", "quiz__course"), public_token=token)
    if attempt.student_id != request.user.id and attempt.quiz.course.teacher_id != request.user.id and not request.user.is_superuser:
        return redirect("dashboard")
    percent = (float(attempt.score or 0) / float(attempt.max_score) * 100) if attempt.max_score else 0
    return render(request, "quiz/result.html", {"attempt": attempt, "percent": round(percent, 1)})

@login_required
def report(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id, course__teacher=request.user)
    attempts = quiz.attempts.filter(submitted_at__isnull=False).select_related("student").order_by("-submitted_at")
    average = attempts.aggregate(avg=Avg("score"))["avg"] or 0
    return render(request, "quiz/report.html", {"quiz": quiz, "attempts": attempts, "average": round(float(average), 2)})

@login_required
def publish_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id, course__teacher=request.user)
    if request.method == "POST":
        quiz.is_published = True
        quiz.save(update_fields=["is_published"])
        messages.success(request, "Quiz published.")
    return redirect("dashboard")
