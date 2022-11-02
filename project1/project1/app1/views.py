from django.http import HttpResponse
from django.shortcuts import render
from .models import place1
from .models import place2

# Create your views here.
def index(request):
    obj=place1.objects.all()
    obj1=place2.objects.all()
    return render(request,"index.html",{'result':obj,'res':obj1})
# def add(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     mul=x*y
#     div=x/y
#     sub=x-y
#     return render(request,"result.html",{'a':add,'b':mul,'c':div,'d':sub})


