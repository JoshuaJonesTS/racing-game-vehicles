from vehicles.models import Vehicle

def all_vehicles():
    return Vehicle.objects.all()

def vehicle(id):
    return Vehicle.objects.get(id=id)