from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import BankAccount
from .serializers import BankAccountSerializer


class BankAccountInformation(ListAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
