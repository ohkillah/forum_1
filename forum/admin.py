from django.contrib import admin

from forum.models import (
    Category,
    Topic,
    Message,
)

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Message)