from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect

# Create your views here.
def home(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'tasks':tasks, 'form':form}
    return render(request, 'list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form':form}
    
    return render(request, 'update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect("/")

    context = {'item':item}

    return render(request, 'delete.html', context)