from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event, Ticket
from .serializers import UserSerializer, EventSerializer, TicketPurchaseSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission


User = get_user_model()
class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "Admin"
# User Registration View
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        serializer.save(password=make_password(password))

# Event List/Create View (Admin Only for POST, All for GET)
class EventListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]  

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminRole()]
        return [permissions.AllowAny()]

# Ticket Purchase View (User Only)
class PurchaseTicketView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        try:
            event = Event.objects.get(pk=id)
            # if event is not available then throwing error 'Event not found'
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TicketPurchaseSerializer(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data['quantity']
            # if quantity is more than available tickets then throwing error 'Not enough tickets available'
            if event.tickets_sold + quantity > event.total_tickets:
                return Response({'error': 'Not enough tickets available'}, status=status.HTTP_400_BAD_REQUEST)

            # Create ticket and update event tickets_sold
            Ticket.objects.create(user=request.user, event=event, quantity=quantity)
            event.tickets_sold += quantity
            event.save()

            return Response({'message': 'Tickets purchased successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
