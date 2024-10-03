from django import forms

class OrderForm(forms.Form):
    legs = forms.IntegerField(min_value=0, label="Legs")
    wings = forms.IntegerField(min_value=0, label="Wings")
    flesh = forms.IntegerField(min_value=0, label="Flesh Portions")