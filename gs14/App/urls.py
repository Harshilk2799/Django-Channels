from django.urls import path
from App import views

urlpatterns = [
    path("<str:group_name>/", views.index)
]
