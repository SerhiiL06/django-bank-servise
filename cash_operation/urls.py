from django.urls import path
from . import views


urlpatterns = [
    path("", views.RefillAndWithdrawalCash.as_view()),
    path("money-send/", views.MoneyTransfer.as_view()),
]
