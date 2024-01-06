from rest_framework import serializers
from .models import Producer
from .models import Transporters
from .models import Owner
from .models import Wood

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'
class TransportersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporters
        fields = '__all__'
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'
class WoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wood
        fields = '__all__'