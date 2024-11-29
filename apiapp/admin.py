from django.contrib import admin
from django.db.models import Sum
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'amount', 'date', 'expiration_date')  # Columns to display
    list_filter = ('date', 'expiration_date')  # Filters in the sidebar
    search_fields = ('title', 'subtitle')  # Searchable fields
    readonly_fields = ('total_balance',)  # Make total_balance a read-only field

    def changelist_view(self, request, extra_context=None):
        # Calculate total balance
        total_balance = Transaction.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        # Pass balance to the admin template context
        extra_context = extra_context or {}
        extra_context['total_balance'] = total_balance
        return super().changelist_view(request, extra_context=extra_context)

    def total_balance(self, obj=None):
        # You can either calculate total balance here or access the extra_context in the template
        return Transaction.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_balance.short_description = "Total Balance"

# Register the Transaction model with the custom admin
admin.site.register(Transaction, TransactionAdmin)
