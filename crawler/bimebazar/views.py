import requests

from django.shortcuts import render
from django.http import HttpResponse

from .models import VehicleBrand, VehicleModel

def car_list(request):
    response = requests.get('https://bimebazar.com/order/api/car-list/')
    if response.status_code == 200:
        vehicle_list = response.json()
        for vehicle_type, brands in vehicle_list.items():
            for brand in brands:
                try:
                    vehicle_brand, _ = VehicleBrand.objects.get_or_create(slug=brand['name_en'], defaults=dict(
                        name=brand['name'],
                        usage_count=brand['uses'],
                    ))
                    for model in brand['models']:
                        VehicleModel.objects.get_or_create(slug=model['name_en'], defaults=dict(
                            name=model['name'],
                            vehicle_type=vehicle_type,
                            vehicle_brand=vehicle_brand,
                        ))
                except:
                    continue

    return render(request, 'bimebazar/vehicles.html', context={
        'vehicle_brands': VehicleBrand.objects.all()
    })
