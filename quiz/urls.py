from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="quiz/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("quiz/<int:quiz_id>/", views.quiz_detail, name="quiz_detail"),
    path("quiz/<int:quiz_id>/take/", views.take_quiz, name="take_quiz"),
    path("quiz/<int:quiz_id>/publish/", views.publish_quiz, name="publish_quiz"),
    path("quiz/<int:quiz_id>/report/", views.report, name="report"),
    path("result/<uuid:token>/", views.result, name="result"),
]
