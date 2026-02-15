from django.shortcuts import redirect, render

from .forms import TodoForm
from .models import Todo

# Create your views here.

def index(request):
    if request.method == 'POST':
        if request.POST['action'] == 'toggle_finished':
            todo = Todo.objects.get(id=request.POST.get('id'))
            todo.finished = not todo.finished
            todo.save()
            return redirect('/todo/')

        # elif request.POST['action'] == 'add_todo':
        #     Todo.objects.create(name=request.POST.get('name', 'No name provided'))
        #     return redirect('/todo/')

        elif request.POST['action'] == 'add_todo':
            form = TodoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/todo/') # Redirect-After-Post!

        elif request.POST['action'] == 'delete_todo':
            todo = Todo.objects.get(id=request.POST.get('id'))
            todo.delete()
            return redirect('/todo/')

    todos = Todo.objects.all()
    form = TodoForm()
    return render(request, 'todoapp/index.html', {'todos': todos, 'form': form})
