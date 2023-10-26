from django.shortcuts import render
from .models import Chat, Group

# Create your views here.
def index(request, groupName):
    print("Group Name: ", groupName)
    group = Group.objects.filter(name=groupName).first()
    chats = []
    if group:
        chats = Chat.objects.filter(group=group)
    else:
        group = Group(name = groupName)
        group.save()
    return render(request, "app/index.html", {"groupName":groupName, "chats": chats})