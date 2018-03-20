from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'blog2/index.html',{'name':'blog2'})

