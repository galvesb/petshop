from pets_app.repositories.pet_repository import PetRepository

class PetUseCases:
    def __init__(self):
        self.pet_repository = PetRepository()

    def list_pets(self):
        return self.pet_repository.get_all()

    def get_pet(self, pk):
        return self.pet_repository.get_by_id(pk)

    def create_pet(self, pet_data):
        return self.pet_repository.create(pet_data)

    def update_pet(self, pk, pet_data):
        pet = self.pet_repository.get_by_id(pk)
        return self.pet_repository.update(pet, pet_data)

    def delete_pet(self, pk):
        pet = self.pet_repository.get_by_id(pk)
        return self.pet_repository.delete(pet)
