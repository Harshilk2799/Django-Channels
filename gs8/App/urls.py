from django.urls import path
from App import views

urlpatterns = [
    path("<str:groupName>/", views.index),
]
