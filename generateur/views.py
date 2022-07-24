from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,  'generateur\home.html', {'MDP': '123456'})

def test(request):
    return HttpResponse('Test')