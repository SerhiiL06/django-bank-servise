from users.models import User
from .serializers import UserDetailSerializer
from rest_framework.generics import RetrieveAPIView


class DetailUserAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
