from rest_framework_simplejwt.views import  TokenRefreshView
from django.urls import path
from .views import RegisterUserView, CustomTokenObtainPairView
urlpatterns = [
    path('user/', RegisterUserView.as_view(), name='register_user'),  # Register API
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login API
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token API
]