import random
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from listings.serializers import serialize_properties
from listings.models import Property

def index(request):
    properties = Property.objects.all()
    random.shuffle(list(properties))
    
    return JsonResponse(serialize_properties(properties[:6]), safe=False)
