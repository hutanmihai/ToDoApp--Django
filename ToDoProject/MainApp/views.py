from django.shortcuts import render, redirect
from .forms import RegisterForm, TodoForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Todo

# Create your views here.

@login_required(login_url='/login')
def home(request):
    todos = Todo.objects.filter(author=request.user).order_by('-important','date','created_at')
    if request.method == 'POST':
        todo_id = request.POST.get('todo-id')
        todo = Todo.objects.filter(id=todo_id)
        todo.delete()
    return render(request, 'MainApp/home.html', {'todos': todos})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('/home')
    else:
        form = TodoForm()
    return render(request, 'MainApp/create_todo.html', {'form': form})