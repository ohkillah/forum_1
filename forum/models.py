from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=1000)
    blocked = models.BooleanField(default=False)
    category_icon = models.CharField(
        max_length=1000, default='default.png',  blank=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    text = models.TextField(default="", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(null=True)
    upvoted_users = models.ManyToManyField(
        User, related_name="upvoted_topics", default=[])
    downvoted_users = models.ManyToManyField(
        User, related_name="downvoted_topics", default=[])
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category}: {self.name}"

    def get_votes(self):
        return self.upvoted_users.count() - self.downvoted_users.count()


class Message(models.Model):
    reply_to = models.ForeignKey(
        "Message", on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.topic}: {self.text}"
