from django.shortcuts import render

# Create your views here.
def index(request, groupName):
    return render(request, "app/index.html", {"groupname": groupName})