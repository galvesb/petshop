from rest_framework import serializers
from pets_app.models.pet import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
