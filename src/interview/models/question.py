from django.db import models
from shortuuid.django_fields import ShortUUIDField


class Difficutly(models.TextChoices):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'


class Question(models.Model):
    """The static Question Bank serves as a fallback or seed for general questions."""

    id = ShortUUIDField(primary_key=True)
    job_type = models.ManyToManyField("interview.JobType", related_name="qsn_job_types", null=True, blank=True)
    skill = models.JSONField(null=True, blank=True)
    difficult_level = models.CharField(max_length=32, choices=Difficutly.choices, default=Difficutly.EASY)
    text = models.CharField(max_length=1024)
    answer_guidelines = models.CharField(max_length=500, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'question'
        default_related_name = 'questions'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class UserQuestion(models.Model):
    """This model tracks tailored questions generated for or assigned to a specific user."""

    id = ShortUUIDField(primary_key=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="user_questions")
    job_type = models.ManyToManyField("interview.JobType", related_name="user_qsn_job_types", null=True, blank=True)
    skill = models.JSONField(null=True, blank=True)
    text = models.CharField(max_length=1024)
    answer_guidelines = models.CharField(max_length=500, null=True, blank=True)
    is_practiced = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_question'
        default_related_name = 'user_questions'
        verbose_name = 'User Question'
        verbose_name_plural = 'User Questions'