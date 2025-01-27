from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import logging
from django.contrib.auth import get_user_model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','role']


logger = logging.getLogger(__name__)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # class method is a decorator which converts a method into a class method which allows it call the method on class level instead of instance level
    @classmethod
    def get_token(cls, user):
        print(f"Generating token for user: {user.email}")

        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        print(token)
        return token

    def validate(self, attrs):
        credentials = {
            'email': attrs.get('username'),  # Change to 'email' if frontend sends email
            'password': attrs.get('password')
        }
    
        
        users = User.objects.all()
        user = None
        for user1 in users:
            print(f"Comparing {user1.username} with {credentials['email']}")
            if user1.username.lower() == credentials['email'].lower():
                print("Match found!")
                user = user1
                break
        else:
            print("No matching user found")
        print(user)
        if not user or not user.check_password(credentials['password']):
            print("Invalid password")
            raise serializers.ValidationError('Invalid credentials')
        else:
            print("Password is correct")
        print("HERE", attrs)
        data = super().validate(attrs)
        print("data",data)

    # get_token will be automatically called within parent validate method
        return data
