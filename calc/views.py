from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name':'navin'})
    # return HttpResponse("hello world")
def add(request):
    value1 = int(request.POST['num2'])
    value2 = int(request.POST['num1'])
    res = value1 + value2
    return render(request, 'result.html', {'result': res})