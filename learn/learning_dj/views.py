from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dj_learn(request):
  learn = 'Django'
  Tclass = 64
  seat = 1
  duration = '1 weak'
  learning = {'c' : learn, 'tl' : Tclass, 'st' : seat, 'cd' : duration}
  return render(request, 'learning_dj/learning_dj.html', context=learning)
def random(request):
  return render(request, 'learning_dj/random_forest.html')
def knn(request):
  return render(request, 'learning_dj/knn.html')
def dt(request):
  return render(request, 'learning_dj/DT.html')
def teacher(request):
  Teachers = {'names' : ['Hijbullah', 'Rony', 'Abir', 'Arif'] }
  return render(request, 'learning_dj/teacher.html', context= Teachers)
def machine(request):
  return render(request, 'learning_dj\machine_learning.html')