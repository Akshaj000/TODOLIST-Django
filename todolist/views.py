from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import auth


def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.created_date = timezone.now()
            task.save()
            return redirect('taskslist')
    else:
        form = TaskForm()
    return render(request, 'todolist/taskform.html', {'form': form})

def task_edit(request,pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.created_date = timezone.now()
            task.save()
            return redirect('taskslist')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todolist/taskform.html', {'form': form})

# def task_check(request,pk):
#     task = get_object_or_404(Task, pk = pk)
#     if request.method == "POST":
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.text = Task.text()
#             task.description = Task.description()
#             task.user = request.user
#             task.created_date = timezone.now()
#             task.save()
#             return redirect('taskslist')
#     else:
#         form = TaskForm(instance=task)
#     return render(request, 'todolist/tasklist.html', {'form': form})

def task_delete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method =="POST":
        task.delete()
        return redirect('taskslist')

    return render(request, "todolist/deletetask.html", {'Task': task})

def tasklist(request):
    tasklist = Task.objects.all()
    return render(request, 'todolist/tasklist.html', {'tasklist': tasklist})

def taskdetail(request, task_id):
    task = get_object_or_404(Task, pk= task_id)
    return render(request, 'todolist/taskdetail.html', {'Task': task})

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'accounts/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('taskslist')
        else:
            return render (request,'todolist/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'todolist/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('taskslist')
        else:
            return render (request,'todolist/signup.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'todolist/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')
