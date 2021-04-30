from django.http import HttpResponse
from django.shortcuts import render

def sample(request):
    return HttpResponse("Hello all")


def con(request):
    return render(request,"sample.html")
    
    
    
