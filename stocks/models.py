from django.db import models

# Create your models here.
class UserSessionId(models.Model):
    session_id = models.CharField(max_length=32)

class StockDetail(models.Model):
    stock = models.CharField(max_length=255, unique=True)
    user = models.ManyToManyField(UserSessionId)

from django.db import models

class Trade(models.Model):
    BUY = 'buy'
    SELL = 'sell'
    SIDE_CHOICES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]

    ticker = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    side = models.CharField(max_length=4, choices=SIDE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticker} - {self.side} - {self.quantity} @ {self.price}"
