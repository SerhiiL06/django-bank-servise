from . import views
from django.urls import path

urlpatterns = [
    path(
        "test/",
        views.BankAccountInformation.as_view(),
    )
]
