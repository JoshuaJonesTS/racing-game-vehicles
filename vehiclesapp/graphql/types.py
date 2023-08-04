from graphene_django import DjangoObjectType
from vehiclesapp.models import Vehicle
import graphene
from .resolvers import vehicle

@key("id")
class VehicleType(DjangoObjectType):

    class Meta:
        model = Vehicle
        fields = ("__all__")

    def _resolve_reference(self, info):
        return Vehicle.objects.get(id=self.id)
