from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Event, Ticket

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TicketPurchaseSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
