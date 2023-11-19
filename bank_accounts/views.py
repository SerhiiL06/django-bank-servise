from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import BankAccount
from .serializers import BankAccountSerializer
from rest_framework import permissions


class BankAccountPrivateInformation(RetrieveAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        account = BankAccount.objects.get(owner=self.request.user)
        return account
