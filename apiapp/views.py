from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer
from datetime import timedelta
from django.utils.timezone import now

class CoinBalanceView(APIView):
    def get(self, request):
        # Calculate the total balance.
        balance = sum([t.amount for t in Transaction.objects.all()])
        # Count coins expiring within 30 days.
        expiring_coins = Transaction.objects.filter(
            expiration_date__gt=now().date(),
            expiration_date__lte=now().date() + timedelta(days=30)
        ).count()

        return Response({
            "balance": balance,
            "expiring_coins": expiring_coins
        }, status=status.HTTP_200_OK)

class TransactionListView(APIView):
    def get(self, request):
        # Retrieve all transactions and serialize them.
        transactions = Transaction.objects.all().order_by('-date')
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
