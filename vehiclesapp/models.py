from django.db import models

# Create your models here.
import uuid
from django.db import models

class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=15)
    speed = models.IntegerField()
    acceleration = models.IntegerField()
    durability = models.IntegerField()
    handling = models.IntegerField()
    traction = models.IntegerField()

    def __str__(self):
        return self.name
