from pets_app.use_cases.owner_use_cases import OwnerUseCases

class OwnerService:
    def __init__(self):
        self.owner_use_cases = OwnerUseCases()

    def list_owners(self):
        return self.owner_use_cases.list_owners()

    def get_owner(self, pk):
        return self.owner_use_cases.get_owner(pk)

    def create_owner(self, owner_data):
        return self.owner_use_cases.create_owner(owner_data)

    def update_owner(self, pk, owner_data):
        return self.owner_use_cases.update_owner(pk, owner_data)

    def delete_owner(self, pk):
        return self.owner_use_cases.delete_owner(pk)
