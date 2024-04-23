from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function that takes a Request and return a Response
# request -> response === Request Handler
# action

def say_hello (request):
  # return HttpResponse("Hello World !!")
  return render(request, 'hello.html', {'name': 'AHMED'})


