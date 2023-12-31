from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # Joser
    path("auth/", include("djoser.urls")),
    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # users app
    path("users/", include("users.urls")),
    path("bank/", include("bank_accounts.urls")),
    # operations
    path("terminal/", include("cash_operation.urls")),
]
