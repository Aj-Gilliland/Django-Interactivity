
from django import forms 

class aForm(forms.Form):
    word = forms.CharField()
    positive_number = forms.IntegerField()

class bForm(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()
    num3 = forms.IntegerField()

class cForm(forms.Form):
    stringThing = forms.CharField()

class dForm(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()
    num3 = forms.IntegerField()   
    num4 = forms.IntegerField()
    num5 = forms.IntegerField()