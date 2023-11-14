from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from typing import List
from dataclasses import dataclass
from .forms import aForm ,bForm ,cForm ,dForm


def aView (request:HttpRequest)->render:
    form = aForm(request.GET)
    if form.is_valid():
        str = form.cleaned_data['word']
        n = form.cleaned_data['positive_number']
        copy_amount = 3
        if copy_amount > len(str):
            copy_amount = len(str)
        copy = str[:copy_amount]
        result = ""
        for i in range(n):
            result = result + copy
        newString = result
        return render(request, "a.html", {'form':form, 'newString': newString})
    else:
        return render(request, "a.html", {'form':form})

def bView (request:HttpRequest)->render:
    def answer(num1, num2, num3):
        return fix_teen(num1) + fix_teen(num2) + fix_teen(num3)
    def fix_teen(n):
        if n == 13 or n == 14 or n == 17 or n == 18 or n == 19:
            return 0
        else:
            return n
    form = bForm(request.GET)
    if form.is_valid():
        num1 = form.cleaned_data['num1']
        num2 = form.cleaned_data['num2']
        num3 = form.cleaned_data['num3']
        return render(request, "b.html", {'form':form, 'number':answer(num1,num2,num3)})
    else:
        return render(request, "b.html", {'form':form})

def cView (request:HttpRequest)->render:
    def xyz_there(str):
        if str[:3] == "xyz":
            return True                
        for i in range(1, len(str) - 2):
            if str[i-1] != "." and str[i:i+3] == "xyz":
                return True                             
        return False
    form = cForm(request.GET)
    if form.is_valid():
        oldString = form.cleaned_data['stringThing']
        return render(request, "c.html", {'form':form, 'newString':xyz_there(oldString)})
    else:
        return render(request, "c.html", {'form':form})

def dView(request:HttpRequest)->render:
    def centered_average(nums):
        return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)
    form = dForm(request.GET)
    if form.is_valid():
        num1 = form.cleaned_data['num1']
        num2 = form.cleaned_data['num2']
        num3 = form.cleaned_data['num3']
        num4 = form.cleaned_data['num4']
        num5 = form.cleaned_data['num5']
        nums = [num1,num2,num3,num4,num5]
        return render(request, "d.html", {'form':form, 'num':centered_average(nums)})
    else:
        return render(request, "d.html", {'form':form})