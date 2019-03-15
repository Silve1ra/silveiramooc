from django.shortcuts import render
from courses.models import Course

# Create your views here.
def courses(request):
    courses = Course.objects.all()
    dados = {
        'courses':courses,
    }
    return render(request, 'courses/courses.html', context=dados)