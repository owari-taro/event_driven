from django.shortcuts import render
from .tasks import long_task,short_task

# Create your views here.

def hello(request):
    print(request)
    long_task.delay(8)
    short_task.delay(1)
    return render(request, 'index.html')