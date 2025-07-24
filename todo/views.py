from django.http import HttpResponse

from django.shortcuts import render
from todo.models import ToDo


def home(request):
    hello = "Assalomu aleykum barcha barchaga, yaxshimisizlar, ahvollaringiz yaxshimi, tinchuxami!"
    tasks = ToDo.objects.all()
    context = {
        'hello1':hello,
        'tasks': tasks
    }
    return render(request, 'todo/home.html', context=context)