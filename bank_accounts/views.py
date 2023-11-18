from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import BankAccount
from .serializers import BankAccountSerializer
from rest_framework import permissions


class BankAccountPrivateInformation(ListAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]
