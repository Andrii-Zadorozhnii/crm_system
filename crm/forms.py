from django import forms
from .models import Clients, Deals


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = [
            'name',
            'email',
            'phone',
            'company'
        ]

class DealsForm(forms.ModelForm):
    class Meta:
        model: Deals
        field = [
            'name',
            'price',
            'status',
            'client'
        ]