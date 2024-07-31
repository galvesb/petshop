
from pets_app.use_cases.pet_use_cases import PetUseCases


class PetService:
    def __init__(self):
        self.pet_use_cases = PetUseCases()

    def list_pets(self):
        return self.pet_use_cases.list_pets()

    def get_pet(self, pk):
        return self.pet_use_cases.get_pet(pk)

    def create_pet(self, pet_data):
        return self.pet_use_cases.create_pet(pet_data)

    def update_pet(self, pk, pet_data):
        return self.pet_use_cases.update_pet(pk, pet_data)

    def delete_pet(self, pk):
        return self.pet_use_cases.delete_pet(pk)
