from django.db import models


class Cryptocurrency(models.Model):
    symbol = models.CharField(max_length=10, unique=True)


class PriceStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ask_price = models.FloatField()
    bid_price = models.FloatField()
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
