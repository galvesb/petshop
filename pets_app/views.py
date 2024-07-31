from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pets_app.models.owner import Owner
from pets_app.models.pet import Pet
from pets_app.serializers.pet_serializer import PetSerializer
from pets_app.serializers.owner_serializer import OwnerSerializer
from pets_app.services.pet_service import PetService
from pets_app.services.owner_service import OwnerService

pet_service = PetService()
owner_service = OwnerService()

@api_view(['GET'])
def list_pets(request):
    pets = pet_service.list_pets()
    serializer = PetSerializer(pets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_pet(request, pk):
    try:
        pet = pet_service.get_pet(pk)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PetSerializer(pet)
    return Response(serializer.data)

@api_view(['POST'])
def create_pet(request):
    serializer = PetSerializer(data=request.data)
    if serializer.is_valid():
        pet_service.create_pet(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_pet(request, pk):
    try:
        pet_service.get_pet(pk)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PetSerializer(data=request.data)
    if serializer.is_valid():
        pet_service.update_pet(pk, serializer.validated_data)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_pet(request, pk):
    try:
        pet_service.get_pet(pk)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    pet_service.delete_pet(pk)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def list_owners(request):
    owners = owner_service.list_owners()
    serializer = OwnerSerializer(owners, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_owner(request, pk):
    try:
        owner = owner_service.get_owner(pk)
    except Owner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = OwnerSerializer(owner)
    return Response(serializer.data)

@api_view(['POST'])
def create_owner(request):
    serializer = OwnerSerializer(data=request.data)
    if serializer.is_valid():
        owner_service.create_owner(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_owner(request, pk):
    try:
        owner_service.get_owner(pk)
    except Owner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = OwnerSerializer(data=request.data)
    if serializer.is_valid():
        owner_service.update_owner(pk, serializer.validated_data)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_owner(request, pk):
    try:
        owner_service.get_owner(pk)
    except Owner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    owner_service.delete_owner(pk)
    return Response(status=status.HTTP_204_NO_CONTENT)
