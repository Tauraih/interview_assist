from django.db import models
from shortuuid.django_fields import ShortUUIDField


class Resume(models.Model):
    id = ShortUUIDField(primary_key=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="resumes")
    resume_file = models.FileField(upload_to="resumes")
    skills = models.JSONField(null=True, blank=True)
    experience = models.JSONField(null=True, blank=True)
    education = models.JSONField(null=True, blank=True)
    other = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'resume'
        default_related_name = 'resumes'
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'
