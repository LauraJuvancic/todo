from django.forms import ModelForm, Textarea, widgets, PasswordInput
import html5.forms.widgets as html5_widgets
from .models import *
from django import forms

class formHome(ModelForm):
    class Meta:
        model = Home
        fields = ('name', 'date', 'info', 'alarm')
        widgets = {
            "date": html5_widgets.DateInput,
        }

class formWork(ModelForm):
    class Meta:
        model = Work
        fields = ('name', 'date', 'info', 'mails', 'workers', 'alarm')

        widgets = {
            "date": html5_widgets.DateInput,
            "info": Textarea(attrs={'rows': 4, 'cols':4}),
            "workers": Textarea(attrs={'rows': 4, 'cols': 4}),
        }


class formPersonal(ModelForm):
    class Meta:
        model = Personal
        fields = ('name', 'date', 'info', 'alarm')
        widgets = {
            "date": html5_widgets.DateInput,
        }

class formTravel(ModelForm):
    class Meta:
        model = Travel
        fields = ('name', 'departure', 'arrival', 'destination', 'pack', 'info', 'alarm')

        widgets = {
            "departure": html5_widgets.DateInput,
            "arrival": html5_widgets.DateInput,
            "pack": Textarea(attrs={'rows': 4, 'cols': 4}),
            "info": Textarea(attrs={'rows': 4, 'cols': 4}),
        }




class formShopping(ModelForm):
    class Meta:
        model = Shopping
        fields = ('name', 'date', 'stuff', 'alarm')
        widgets = {
            "date": html5_widgets.DateInput,
        }

class formBirthday(ModelForm):
    class Meta:
        model = Birthday
        fields = ('name', 'date', 'presents', 'alarm')
        widgets = {
            "date": html5_widgets.DateInput,
        }

class formCooking(ModelForm):
    class Meta:
        model = Cooking
        fields = ('name', 'date', 'ingredients', 'procedure', 'alarm')
        widgets = {
            "date": html5_widgets.DateInput,
            "ingredients": Textarea(attrs={'rows': 10, 'cols': 4}),
            "procedure": Textarea(attrs={'rows': 10, 'cols': 4}),
        }

class formLogin(forms.Form):
    username = forms.CharField(label='Username:', max_length=100)
    password = forms.CharField(label='Geslo:', max_length=100, widget=forms.PasswordInput)

class formSignup(forms.Form):
    first_name = forms.CharField(label="First name:", max_length=30)
    last_name = forms.CharField(label="Last name:", max_length=30)
    email = forms.EmailField()
    username = forms.CharField(label='Username:', max_length=100)
    password = forms.CharField(label='Geslo:', max_length=100, widget=forms.PasswordInput)

class formEditprofile(forms.Form):
    first_name = forms.CharField(label="First name:", max_length=30)
    last_name = forms.CharField(label="Last name:", max_length=30)
    email = forms.EmailField()
    username = forms.CharField(label='Username:', max_length=100)
    password = forms.CharField(label='Geslo:', max_length=100, widget=forms.PasswordInput, required=False)

