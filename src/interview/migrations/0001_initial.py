# Generated by Django 5.1.4 on 2024-12-14 08:50

import django.db.models.deletion
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=22, max_length=22, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Job Category',
                'verbose_name_plural': 'Job Categories',
                'db_table': 'job_category',
                'default_related_name': 'job_category',
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=22, max_length=22, prefix='', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('required_skills', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='interview.jobcategory')),
            ],
            options={
                'verbose_name': 'Job Type',
                'verbose_name_plural': 'Job Types',
                'db_table': 'job_types',
                'default_related_name': 'job_types',
            },
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=22, max_length=22, prefix='', primary_key=True, serialize=False)),
                ('questions', models.JSONField()),
                ('responses', models.JSONField(blank=True, null=True)),
                ('score', models.DecimalField(decimal_places=2, max_digits=100)),
                ('feedback', models.CharField(blank=True, max_length=2048, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_interview', to=settings.AUTH_USER_MODEL)),
                ('job_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interview_job_type', to='interview.jobtype')),
            ],
            options={
                'verbose_name': 'Interview',
                'verbose_name_plural': 'Interviews',
                'db_table': 'interview',
                'default_related_name': 'interviews',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=22, max_length=22, prefix='', primary_key=True, serialize=False)),
                ('skill', models.JSONField(blank=True, null=True)),
                ('difficult_level', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='easy', max_length=32)),
                ('text', models.CharField(max_length=1024)),
                ('answer_guidelines', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job_type', models.ManyToManyField(blank=True, null=True, related_name='qsn_job_types', to='interview.jobtype')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'db_table': 'question',
                'default_related_name': 'questions',
            },
        ),
        migrations.CreateModel(
            name='UserJobPreference',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=22, max_length=22, prefix='', primary_key=True, serialize=False)),
                ('is_primary', models.BooleanField(blank=True, default=None, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_job_types', to='interview.jobtype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_preferences', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Job prefence',
                'verbose_name_plural': 'Job prefences',
                'db_table': 'user_job_preferences',
                'default_related_name': 'Job prefences',
            },
        ),
        migrations.CreateModel(
            name='UserQuestion',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=22, max_length=22, prefix='', primary_key=True, serialize=False)),
                ('skill', models.JSONField(blank=True, null=True)),
                ('text', models.CharField(max_length=1024)),
                ('answer_guidelines', models.CharField(blank=True, max_length=500, null=True)),
                ('is_practiced', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job_type', models.ManyToManyField(blank=True, null=True, related_name='user_qsn_job_types', to='interview.jobtype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Question',
                'verbose_name_plural': 'User Questions',
                'db_table': 'user_question',
                'default_related_name': 'user_questions',
            },
        ),
        migrations.CreateModel(
            name='AIFeedback',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=22, max_length=22, prefix='', primary_key=True, serialize=False)),
                ('response', models.CharField(blank=True, max_length=2048, null=True)),
                ('score', models.IntegerField(default=0)),
                ('strengths', models.CharField(blank=True, max_length=500, null=True)),
                ('improvement_areas', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ai_user_interview', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aifb_questions', to='interview.question')),
                ('user_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aifb_user_question', to='interview.userquestion')),
            ],
            options={
                'verbose_name': 'AI Feedback',
                'verbose_name_plural': 'AI Feedback',
                'db_table': 'ai_feedback',
                'default_related_name': 'ai_feedback',
            },
        ),
    ]
