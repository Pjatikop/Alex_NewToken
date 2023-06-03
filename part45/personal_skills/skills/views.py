from django.shortcuts import render
from .models import Skills


def index(request):
    prog = Skills.objects.all()
    return render(request, 'skills/index.html', {'prog': prog})
