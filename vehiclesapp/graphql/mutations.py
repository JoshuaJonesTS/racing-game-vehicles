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
    class Arguments:
        id = graphene.UUID(required=True)
        name = graphene.String()
        # speed = graphene.Int(),
        acceleration = graphene.Int()
        durability = graphene.Int()
        handling = graphene.Int()
        traction = graphene.Int()

    vehicle = graphene.Field(VehicleType)

    @classmethod
    def mutate(cls, root, info, **kwargs):        
        new_vehicle = Vehicle.objects.get(pk=kwargs.get('id'))

        if 'name' in kwargs:
            new_vehicle.name=kwargs.get('name') 

        if 'speed' in kwargs:
            new_vehicle.speed=kwargs.get('speed') 

        if 'acceleration' in kwargs:
            new_vehicle.acceleration=kwargs.get('acceleration') 

        if 'durability' in kwargs:
            new_vehicle.durability=kwargs.get('durability') 

        if 'handling' in kwargs:
            new_vehicle.handling=kwargs.get('handling') 

        if 'traction' in kwargs:
            new_vehicle.traction=kwargs.get('traction') 

        new_vehicle.save()

        return EditVehicle(vehicle=new_vehicle)
    
class VehicleMutations(graphene.ObjectType):
    create_vehicle = CreateVehicle.Field()
    edit_vehicle = EditVehicle.Field()
