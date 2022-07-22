from django.shortcuts import render
from .models import Todolists

# Create your views here.

def index(request):
    todo_items = Todolists.objects.order_by('id')
    context = {'todo_items' : todo_items}
    return render(request, 'todolists/index.html', context)
    