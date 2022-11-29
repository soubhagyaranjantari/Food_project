from django.shortcuts import render

from accounts.forms import userFormm

# Create your views here.
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')
