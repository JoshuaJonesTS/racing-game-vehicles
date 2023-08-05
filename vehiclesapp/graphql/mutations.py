import graphene
from .types import VehicleType
from vehiclesapp.models import Vehicle

class CreateVehicle(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        speed = graphene.Int(required=True)
        acceleration = graphene.Int(required=True)
        durability = graphene.Int(required=True)
        handling = graphene.Int(required=True)
        traction = graphene.Int(required=True)
       
    vehicle = graphene.Field(VehicleType)

    @classmethod
    def mutate(cls, root, info, **kwargs):    
        new_vehicle = Vehicle.objects.create(
            name = kwargs.get('name'),
            speed = kwargs.get('speed'),
            acceleration = kwargs.get('acceleration'),
            durability = kwargs.get('durability'),
            handling = kwargs.get('handling'),
            traction = kwargs.get('traction'),
        )
        return CreateVehicle(vehicle=new_vehicle)
    
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
