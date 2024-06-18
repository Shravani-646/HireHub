# Generated by Django 4.2.13 on 2024-06-17 04:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobmanager', '0006_skills_remove_jobpost_requirements_jobpost_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.TextField()),
                ('resume', models.FileField(upload_to='jobmanager/applications')),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='jobmanager.jobpost')),
                ('skills', models.ManyToManyField(to='jobmanager.skills')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
