# Generated by Django 3.2.12 on 2022-04-14 07:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_topic_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_icon',
            field=models.CharField(blank=True, default='default.png', max_length=1000),
        ),
        migrations.AddField(
            model_name='topic',
            name='downvoted_users',
            field=models.ManyToManyField(default=[], related_name='downvoted_topics', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topic',
            name='upvoted_users',
            field=models.ManyToManyField(default=[], related_name='upvoted_topics', to=settings.AUTH_USER_MODEL),
        ),
    ]
