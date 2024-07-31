from pets_app.repositories.owner_repository import OwnerRepository

class OwnerUseCases:
    def __init__(self):
        self.owner_repository = OwnerRepository()

    def list_owners(self):
        return self.owner_repository.get_all()

    def get_owner(self, pk):
        return self.owner_repository.get_by_id(pk)

    def create_owner(self, owner_data):
        return self.owner_repository.create(owner_data)

    def update_owner(self, pk, owner_data):
        owner = self.owner_repository.get_by_id(pk)
        return self.owner_repository.update(owner, owner_data)

    def delete_owner(self, pk):
        owner = self.owner_repository.get_by_id(pk)
        return self.owner_repository.delete(owner)
