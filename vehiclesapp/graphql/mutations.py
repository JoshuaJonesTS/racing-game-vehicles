import graphene
from .types import VehicleType
from vehiclesapp.models import Vehicle

class VehicleInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    # speed = graphene.Int(required=False)
    # acceleration = graphene.Int(required=False)
    # durability = graphene.Int(required=False)
    # handling = graphene.Int(required=False)
    # traction = graphene.Int(required=False)

class CreateVehicle(graphene.Mutation):
    class Arguments:
        vehicle_data = VehicleInput(required=True)
    
    vehicle = graphene.Field(VehicleType)

    @classmethod
    def mutate(root, info, vehicle_data=None):    
        vehicle = VehicleType(
            name = vehicle_data.name,
            # speed = vehicle_data.speed,
            # acceleration = vehicle_data.acceleration,
            # durability = vehicle_data.durability,
            # handling = vehicle_data.handling,
            # traction = vehicle_data.traction
        )
        return CreateVehicle(vehicle=vehicle)
    
class EditVehicle(graphene.Mutation):
    class Arguments():
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    vehicle = graphene.Field(VehicleType)

    @classmethod
    def mutate(cls, root, info, id, name):
        try:
            vehicle = Vehicle.objects.get(pk=id)
        except Vehicle.DoesNotExist:
            raise Exception('Vehicle does not exist.')
        
        vehicle.name = name
        vehicle.save()

        return EditVehicle(vehicle=vehicle)
    
class VehicleMutations(graphene.ObjectType):
    create_vehicle = CreateVehicle.Field()
    edit_vehicle = EditVehicle.Field()
