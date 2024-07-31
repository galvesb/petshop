from pets_app.models.owner import Owner

class OwnerRepository:
    def get_all(self):
        return Owner.objects.all()

    def get_by_id(self, pk):
        return Owner.objects.get(pk=pk)

    def create(self, owner_data):
        return Owner.objects.create(**owner_data)

    def update(self, owner, owner_data):
        for key, value in owner_data.items():
            setattr(owner, key, value)
        owner.save()
        return owner

    def delete(self, owner):
        owner.delete()
