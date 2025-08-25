from rest_framework import serializers
from .models import User, Collect, Payment
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PaymentSerializer(serializers.ModelSerializer):
    donor_name = serializers.CharField(source='donor.get_full_name', read_only=True)
    class Meta:
        model = Payment
        fields = ['id', 'collect', 'donor', 'donor_name', 'amount', 'date_time']
        read_only_fields = ['date_time']

class CollectSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)

    class Meta:
        model = Collect
        fields = [
            'id',
            'author',
            'author_name',
            'title',
            'reason',
            'description',
            'target_amount',
            'current_amount',
            'cover_image',
            'end_date'
        ]
