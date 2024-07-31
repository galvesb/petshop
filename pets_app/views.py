from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pet
from .serializers import PetSerializer

@api_view(['GET'])
def list_pets(request):
    pets = Pet.objects.all()
    serializer = PetSerializer(pets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_pet(request, pk):
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PetSerializer(pet)
    return Response(serializer.data)

@api_view(['POST'])
def create_pet(request):
    serializer = PetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_pet(request, pk):
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PetSerializer(pet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_pet(request, pk):
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    pet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
