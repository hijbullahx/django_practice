from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")
def login(request):
    return render(request, "login.html")
def contact(request):
    return render(request, "contact.html")
def features(request):
    return render(request, "features.html")