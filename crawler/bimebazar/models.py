from django.db import models


class AbstractVehicle(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        abstract = True


class VehicleBrand(AbstractVehicle):
    usage_count = models.PositiveIntegerField(default=0)


class VehicleModel(AbstractVehicle):
    CAR, AUTOCAR, CARRIER, MOTORCYCLE = 'car', 'autocar', 'carrier', 'motorcycle'
    VEHICLE_TYPE_CHOICES = [
        (CAR, 'سواری'),
        (AUTOCAR, 'ون'),
        (CARRIER, 'باری'),
        (MOTORCYCLE, 'موتورسیکلت')
    ]
    
    vehicle_brand = models.ForeignKey(VehicleBrand, on_delete=models.SET_NULL, null=True, related_name='vehicle_models')
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)

    def __str__(self):
        return self.name
