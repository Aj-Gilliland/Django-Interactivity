from django import forms 

class heyForm(forms.Form):
    name = forms.CharField()

class ageForm(forms.Form):
    futureYear = forms.IntegerField()
    birthYear = forms.IntegerField()

class orderForm(forms.Form):
    fries = forms.IntegerField()
    burgers = forms.IntegerField()
    drinks = forms.IntegerField()
    