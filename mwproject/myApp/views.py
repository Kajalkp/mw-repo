from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    a=int(input("enter the value of a: "))
    b=int(input("enter the value of b: "))
    print(a/b)
    return HttpResponse("<h1>output on webpage </h1>")
