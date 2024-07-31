from rest_framework import serializers
from pets_app.models.owner import Owner
from pets_app.models.pet import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'species', 'age']

class OwnerSerializer(serializers.ModelSerializer):
    pets = PetSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = '__all__'
