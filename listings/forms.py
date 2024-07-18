from django.forms import ModelForm
from django import forms
from .models import Property
import re
from django.core.exceptions import ValidationError

class PropertyForm(ModelForm):
    type = forms.ChoiceField(
        required=False,	
        widget=forms.RadioSelect,
    )
    type.choices = Property.CATEGORIES

    class Meta:
        model = Property
        fields = ["title", "type", "address", "contact_1", "contact_2","rent_per_month","picture"] 

    def is_ten_digit_number(self, string):
        pattern = r'^\d{10}$'
    
        match = re.match(pattern, string)
    
        return match is not None


    def clean_contact_1(self):
        data = self.cleaned_data["contact_1"]
        if not self.is_ten_digit_number(data):
            raise ValidationError("Enter a valid phone number!!!")
        return data

    def clean_contact_2(self):
        data = self.cleaned_data["contact_2"]
        if data and not self.is_ten_digit_number(data):
            raise ValidationError("Enter a valid phone number!!!")
        return data
     
    """def clean_rent_per_month(self):
        pass"""        