from rest_framework import generics
from django.contrib.auth.hashers import make_password
from .models import User
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# JWT Authentication for login and password
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        role = serializer.validated_data.get('role', 'User')
        is_staff = True if role == "Admin" else False
        serializer.save(
            password=make_password(serializer.validated_data['password']),
            is_staff=is_staff
        )
