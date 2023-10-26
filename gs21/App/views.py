from django.shortcuts import render
from .models import Chat, Group
from channels.layers import get_channel_layer
from django.shortcuts import HttpResponse
from asgiref.sync import async_to_sync

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


def msgfromoutside(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "India",
        {
            "type":"chat.message",
            "message":"Message from Outside Consumer"
        }
    )
    return HttpResponse("Message Send from View to Consumer")