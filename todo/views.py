from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.

def example(request):
    return render(request, 'todo/index.html')


class Notes(ListView):

    pass