from django.urls import path
from .views import list_pets, get_pet, create_pet, update_pet, delete_pet

urlpatterns = [
    path('pets/', list_pets, name='list_pets'),
    path('pets/<int:pk>/', get_pet, name='get_pet'),
    path('pets/create/', create_pet, name='create_pet'),
    path('pets/update/<int:pk>/', update_pet, name='update_pet'),
    path('pets/delete/<int:pk>/', delete_pet, name='delete_pet'),
]
