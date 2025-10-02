from django.shortcuts import render
from django.http import HttpResponse

def blog1(request):
  return render(request, 'learning_dj2/learning_dj2.html')
