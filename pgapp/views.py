from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ntrends(request):
    return HttpResponse("")
def page1(request):
    return render(request,'home.html')
def page2(request):
    return render(request,'form2.html')