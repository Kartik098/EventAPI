from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListCreateView.as_view(), name='event-list-create'),
    path('<int:id>/purchase/', views.PurchaseTicketView.as_view(), name='purchase-ticket'),
]