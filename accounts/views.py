from django.shortcuts import render
from .forms import RegisterationForm

# Create your views here.

def register(request):
  form = RegisterationForm()
  context = {'form': form}
  return render(request, 'accounts/register.html', context)


def login(request):
  context = {}
  return render(request, 'accounts/login.html', context)


def logout(request):
  
  return