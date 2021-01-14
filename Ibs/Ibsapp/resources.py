from import_export import resources
from .models import Member, Inventory

class MemberResource(resources.ModelResource):
    class Meta:
        model = Member

class InventoryResource(resources.ModelResource):
    class Meta:
        model = Inventory