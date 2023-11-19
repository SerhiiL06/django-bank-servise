from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.DetailUserAPIView.as_view()),
    path("search/", views.SearchUserAPIView.as_view()),
]
