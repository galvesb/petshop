from pets_app.models.pet import Pet

class PetRepository:
    def get_all(self):
        return Pet.objects.all()

    def get_by_id(self, pk):
        return Pet.objects.get(pk=pk)

    def create(self, pet_data):
        return Pet.objects.create(**pet_data)

    def update(self, pet, pet_data):
        for key, value in pet_data.items():
            setattr(pet, key, value)
        pet.save()
        return pet

    def delete(self, pet):
        pet.delete()
