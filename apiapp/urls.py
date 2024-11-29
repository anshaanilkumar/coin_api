from django.urls import path
from .views import CoinBalanceView, TransactionListView

urlpatterns = [
    path('balance/', CoinBalanceView.as_view(), name='coin-balance'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
]
