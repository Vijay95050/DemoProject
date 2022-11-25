from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(req):
    return HttpResponse("<h1>Hello from DemoApp1 f1()..</h1><hr />")
def f2(req):
    return HttpResponse("<h1> Hello from DemoApp2 f2().. and Have a nice day</h1><hr />")
