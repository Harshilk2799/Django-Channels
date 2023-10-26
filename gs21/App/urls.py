from django.urls import path 
from . import views

urlpatterns = [
    path("<str:groupName>/", views.index),
    path("test/vtoc/", views.msgfromoutside),
]