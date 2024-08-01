import random
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse
from .models import Property
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .forms import PropertyForm
from listings.serializers import serialize_properties
class MainView(View):

    def get(self, request):
        properties = Property.objects.all()
        properties = list(properties)
        random.shuffle(properties)
        
        return JsonResponse(serialize_properties(properties), safe=False)

class PropertyCreate(OwnerCreateView):
    model = Property
    form_class = PropertyForm
    success_url = reverse_lazy("user:all")

class PropertyUpdate(OwnerUpdateView):
    model = Property
    fields = ["title", "address", "type", "contact_1", "contact_2","status", "rent_per_month","picture"]
    success_url = reverse_lazy("user:all")

class PropertyDelete(OwnerDeleteView):
    model = Property
    success_url = reverse_lazy("user:all")