from django.db import models
from api.models import User

class Event(models.Model):
    name = models.CharField(max_length=254)
    date = models.DateField()
    total_tickets = models.IntegerField()
    tickets_sold = models.IntegerField()

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)


