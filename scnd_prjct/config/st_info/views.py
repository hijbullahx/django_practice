from django.shortcuts import render
from st_info.models import Student

# Create your views here.
def home(request):
    return render(request, 'index.html')

def add_student(request):
    if request.method == "POST":
        st_id = request.POST.get('st_id')
        st_name = request.POST.get('st_name')
        dept = request.POST.get('dept')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
