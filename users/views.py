from users.models import User
from .serializers import UserDetailSerializer, PublicUserSerializer, AdminUserSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import OwnerOrSuperser


class DetailUserAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [OwnerOrSuperser]
    serializer_class = UserDetailSerializer


class SearchUserAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PublicUserSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        phone_number = self.request.query_params.get("phone")

        update_phone = f"+38{phone_number}"

        queryset = User.objects.filter(phone_number=update_phone)

        return queryset

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return AdminUserSerializer
        return super().get_serializer_class()
