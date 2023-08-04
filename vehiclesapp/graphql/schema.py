import graphene
from vehiclesapp.models import Vehicle
from .types import *
from .resolvers import *

class VehicleQueries(graphene.ObjectType):
    all_vehicles = graphene.List(VehicleType)
    vehicle = graphene.Field(VehicleType, id=graphene.ID())

    def resolve_all_vehicles(cls, info):
        return all_vehicles()
    
    def resolve_vehicle(cls, info, id):
        return vehicle(id)