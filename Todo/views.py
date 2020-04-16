from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Todo
from .forms import TodoForm
from django.utils import timezone

@login_required
def todo(request):
    todos = Todo.objects.filter(user=request.user , datecompleted__isnull=True ).order_by('-created')
    context = {
        'todos':todos
    }
    return render(request,'Todo/todo.html',context)

@login_required
def createtodo(request):
    if request.method == 'POST':
        form    = TodoForm(request.POST)
        newTodo = form.save(commit=False)
        newTodo.user = request.user
        newTodo.save()
        return redirect('Todo:todo')
    else:
        form = TodoForm()
    return render(request ,'Todo/createtodo.html', {'form':form})

def viewtodo(request,pk):
    todo = get_object_or_404(Todo,pk=pk,user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance = todo)
        form.save()
        context = {
            'todo':todo,
            'form':form,
        }
        return redirect('Todo:todo')
    else:
        form = TodoForm(instance=todo)
        context = {
            'todo':todo,
            'form':form
        }
        return render(request,'Todo/viewtodo.html',context)

def completetodo(request,pk):
    todo = get_object_or_404(Todo, pk=pk,  user = request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('Todo:todo')

def deletetodo(request,pk):
    todo = get_object_or_404(Todo , pk=pk , user = request.user  )
    if request.method == 'POST':
        todo.delete()
        return redirect('Todo:todo')


def completelisttodo(request):
    todos = Todo.objects.filter(user=request.user , datecompleted__isnull=False ).order_by('-created')
    context = {
        'todos':todos
    }
    return render(request,'Todo/completelisttodo.html',context)