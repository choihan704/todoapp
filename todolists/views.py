from django.shortcuts import render, redirect
from .models import Todolists
from .forms import TodoListForm
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    todo_items = Todolists.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items' : todo_items, 'form' : form}
    return render(request, 'todolists/index.html', context)
    
@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)

    #print(request.POST['text'])
    if form.is_valid():
        new_todo = Todolists(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completedTodo(request, todo_id):
    todo = Todolists.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todolists.objects.filter(completed__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todolists.objects.all().delete()

    return redirect('index')