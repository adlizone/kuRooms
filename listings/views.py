from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse
from .models import Property
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .forms import PropertyForm

class MainView(OwnerListView):
    model = Property
    fields = ["title", "address", "contact_1", "contact_2", "rent_per_month"]

class PropertyCreate(OwnerCreateView):
    model = Property
    form_class = PropertyForm
    success_url = reverse_lazy("user:all")

class PropertyUpdate(OwnerUpdateView):
    model = Property
    fields = ["title", "address", "type", "contact_1", "contact_2", "rent_per_month"]
    success_url = reverse_lazy("user:all")

class PropertyDelete(OwnerDeleteView):
    model = Property
    success_url = reverse_lazy("user:all")