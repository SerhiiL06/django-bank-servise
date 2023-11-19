from django.urls import path
from . import views


urlpatterns = [
    path("", views.RefillAndWithdrawalCash.as_view()),
]
