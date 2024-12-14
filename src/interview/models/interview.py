from django.db import models
from shortuuid.django_fields import ShortUUIDField


class Interview(models.Model):
    """Tracks user practice sessions."""

    id = ShortUUIDField(primary_key=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="user_interview")
    job_type = models.ForeignKey("interview.JobType", on_delete=models.SET_NULL, related_name="interview_job_type", null=True, blank=True)
    questions = models.JSONField()
    responses = models.JSONField(null=True, blank=True)
    score = models.DecimalField(max_digits=100, decimal_places=2)
    feedback = models.CharField(max_length=2048, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'interview'
        default_related_name = 'interviews'
        verbose_name = 'Interview'
        verbose_name_plural = 'Interviews'


class AIFeedback(models.Model):
    """Tracks user practice sessions."""

    id = ShortUUIDField(primary_key=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="ai_user_interview")
    question = models.ForeignKey("interview.Question", on_delete=models.CASCADE, related_name='aifb_questions')
    user_question = models.ForeignKey("interview.UserQuestion", on_delete=models.CASCADE, related_name='aifb_user_question')
    response = models.CharField(max_length=2048, null=True, blank=True)
    score = models.IntegerField(default=0)
    strengths = models.CharField(max_length=500, null=True, blank=True)
    improvement_areas = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'ai_feedback'
        default_related_name = 'ai_feedback'
        verbose_name = 'AI Feedback'
        verbose_name_plural = 'AI Feedback'
