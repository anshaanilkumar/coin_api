from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    expiration_text = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['id', 'title', 'subtitle', 'amount', 'date', 'expiration_date', 'expiration_text']

    def get_expiration_text(self, obj):
        return obj.get_expiration_text()
