from django.db import models
from django.utils.timezone import now

class Transaction(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    amount = models.IntegerField()
    date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)

    def get_expiration_text(self):
        """Calculate how far the expiration date is from the current date."""
        if self.expiration_date:
            days_left = (self.expiration_date - now().date()).days
            if days_left > 0:
                return f"Expires in {days_left} days"
            elif days_left == 0:
                return "Expires today"
            else:
                return f"Expired {abs(days_left)} days ago"
        return "No expiration date"
