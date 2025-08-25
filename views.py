from rest_framework import viewsets, permissions
from .models import Collect, Payment
from .serializers import CollectSerializer, PaymentSerializer
class CollectViewSet(viewsets.ModelViewSet):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(donor=self.request.user)
        collect_instance = payment.collect
        collect_instance.current_amount += payment.amount
        collect_instance.save()
        
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
