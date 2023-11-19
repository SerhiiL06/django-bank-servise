from . import views
from django.urls import path

urlpatterns = [
    path(
        "myself/",
        views.BankAccountPrivateInformation.as_view(),
    )
]
