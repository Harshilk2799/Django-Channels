from django.contrib import admin
from .models import Group, Chat

@admin.register(Chat)
class ChatModelAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "timestamp", "group"]


@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]