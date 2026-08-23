from django.contrib import admin
from django.urls import path

from core import views


urlpatterns = [

    # ============================================================
    # HOME
    # ============================================================

    path(
        "",
        views.home,
        name="home"
    ),


    # ============================================================
    # AUTHENTICATION
    # ============================================================

    path(
        "register/",
        views.register_view,
        name="register"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),


    # ============================================================
    # HISTORY
    # ============================================================

    path(
        "history/",
        views.history,
        name="history"
    ),


    # ============================================================
    # RESUME ANALYZER
    # ============================================================

    path(
        "resume-analyzer/",
        views.resume_analyzer,
        name="resume_analyzer"
    ),

    # Alias
    # /resume/ also opens the resume analyzer.
    path(
        "resume/",
        views.resume_analyzer,
        name="resume"
    ),


    # ============================================================
    # VIEW RESUME FROM HISTORY
    # ============================================================

    path(
        "resume/<int:resume_id>/",
        views.view_resume,
        name="view_resume"
    ),


    # ============================================================
    # ADMIN
    # ============================================================

    path(
        "admin/",
        admin.site.urls
    ),
]