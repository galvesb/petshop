from django.urls import path
from .views import list_pets, get_pet, create_pet, update_pet, delete_pet
from .views import list_owners, get_owner, create_owner, update_owner, delete_owner

urlpatterns = [
    path('pets/', list_pets, name='list_pets'),
    path('pets/<int:pk>/', get_pet, name='get_pet'),
    path('pets/create/', create_pet, name='create_pet'),
    path('pets/update/<int:pk>/', update_pet, name='update_pet'),
    path('pets/delete/<int:pk>/', delete_pet, name='delete_pet'),
    path('owners/', list_owners, name='list_owners'),
    path('owners/<int:pk>/', get_owner, name='get_owner'),
    path('owners/create/', create_owner, name='create_owner'),
    path('owners/update/<int:pk>/', update_owner, name='update_owner'),
    path('owners/delete/<int:pk>/', delete_owner, name='delete_owner'),
]
