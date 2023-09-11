from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

from .serializers import OrderSerializer
from .models import Order


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'receiver', 'sender']
    ordering_fields = ['status', 'receiver', 'sender']