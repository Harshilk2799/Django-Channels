from django.shortcuts import render

# Create your views here.
def index(request, groupName):
    print("Group Name: ", groupName)
    return render(request, "app/index.html", {"groupName":groupName})