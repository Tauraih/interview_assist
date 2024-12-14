from django.db import models
from shortuuid.django_fields import ShortUUIDField


class JobCategory(models.Model):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'job_category'
        default_related_name = 'job_category'
        verbose_name = 'Job Category'
        verbose_name_plural = 'Job Categories'


class JobType(models.Model):
    id = ShortUUIDField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    required_skills = models.JSONField(null=True, blank=True)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name="categories")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'job_types'
        default_related_name = 'job_types'
        verbose_name = 'Job Type'
        verbose_name_plural = 'Job Types'


class UserJobPreference(models.Model):
    id = ShortUUIDField(primary_key=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="job_preferences")
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE, related_name='user_job_types')
    is_primary = models.BooleanField(default=None, null=True, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_job_preferences'
        default_related_name = 'Job prefences'
        verbose_name = 'Job prefence'
        verbose_name_plural = 'Job prefences'
