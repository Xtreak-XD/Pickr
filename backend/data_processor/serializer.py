from rest_framework import serializers
from .models import techItems, carParts, toys, clothesItems, forYouPage

class automotiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = carParts
        fields = '__all__'

class techItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = techItems
        fields = '__all__'

class toysSerializer(serializers.ModelSerializer):
    class Meta:
        model = toys
        fields = '__all__'

class clothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = clothesItems
        fields = '__all__'

class forYouPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = forYouPage
        fields = '__all__'