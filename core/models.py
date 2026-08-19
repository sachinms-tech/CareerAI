from django.db import models
from django.contrib.auth.models import User


# ============================================================
# CAREER SEARCH HISTORY
# ============================================================

class CareerSearch(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    career = models.CharField(
        max_length=200
    )

    source = models.CharField(
        max_length=50
    )

    searched_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.career


# ============================================================
# RESUME ANALYSIS
# ============================================================

class ResumeAnalysis(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    resume = models.FileField(
        upload_to="resumes/"
    )

    extracted_text = models.TextField(
        blank=True
    )

    analyzed_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - Resume"