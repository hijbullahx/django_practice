from django.urls import path
from . import views
urlpatterns = [
    path('machine',views.dj_learn),
    path('random',views.random),
    path('knn',views.knn),
    path('dt',views.dt),
    path('teacher', views.teacher),
    path('mll', views.machine)

]