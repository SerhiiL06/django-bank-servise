from . import views
from django.urls import path

urlpatterns = [
    path(
        "test/",
        views.BankAccountPrivateInformation.as_view(),
    )
]
