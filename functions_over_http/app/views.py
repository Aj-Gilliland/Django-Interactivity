from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from typing import List
from dataclasses import dataclass
from .forms import heyForm, ageForm, orderForm

def heyView (request:HttpRequest)->render:
    form = heyForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']
        return render(request, "heyHtml.html", {'form':form, 'name': request.GET['name']})
    else:
        return render(request, "heyHtml.html", {'form':form})

def ageView (request:HttpRequest)->render:
    form = ageForm(request.GET)
    if form.is_valid():
        ageDiff = (int(form.cleaned_data['futureYear'])-int(form.cleaned_data['birthYear']))
        return render(request, "ageHtml.html", {'form':form,'age':ageDiff})
    else:
        return render(request, "ageHtml.html", {'form':form})
    
def orderView (request:HttpRequest)->render:
    form = orderForm(request.GET)
    if form.is_valid():
        orderTotal = (1.5*form.cleaned_data['fries'])+(4.5*form.cleaned_data['burgers'])+(form.cleaned_data['drinks'])
        return render(request, "orderHtml.html", {'form':form, 'orderTotal':orderTotal}) 
    else:
        return render(request, "orderHtml.html", {'form':form,}) 