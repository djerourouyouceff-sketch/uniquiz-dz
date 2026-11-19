from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid

class Course(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="courses")
    name = models.CharField(max_length=160)
    code = models.CharField(max_length=20, unique=True)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="enrolled_courses")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} ({self.code})"

class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="quizzes")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(default=20)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title

class Question(models.Model):
    SINGLE = "single"
    TRUE_FALSE = "true_false"
    TYPE_CHOICES = [(SINGLE, "Single choice"), (TRUE_FALSE, "True / False")]
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    question_type = models.CharField(max_length=12, choices=TYPE_CHOICES, default=SINGLE)
    points = models.DecimalField(max_digits=6, decimal_places=2, default=1)
    order = models.PositiveIntegerField(default=1)
    def __str__(self): return self.text[:70]

class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=1)
    def __str__(self): return self.text[:70]

class Attempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="attempts")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="quiz_attempts")
    started_at = models.DateTimeField(default=timezone.now)
    submitted_at = models.DateTimeField(null=True, blank=True)
    score = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    max_score = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    public_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["quiz", "student"], name="one_attempt_per_student_quiz")]
    def __str__(self): return f"{self.student} - {self.quiz}"

class Response(models.Model):
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE, related_name="responses")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(AnswerOption, null=True, blank=True, on_delete=models.SET_NULL)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["attempt", "question"], name="one_response_per_question")]
