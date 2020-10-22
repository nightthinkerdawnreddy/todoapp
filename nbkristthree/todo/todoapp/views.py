from django.shortcuts import render,HttpResponse,redirect
from .models import Todo

# Create your views here.
def home(request):
    if request.method == 'POST':
        task = request.POST.get("task",False)
        Todo.objects.create(task=task)
    objs = Todo.objects.all()
    print(objs)
    return render(request,"home.html",{"objs":objs})

def delete(request,keyid):
    obj = Todo.objects.filter(id=keyid)
    obj.delete()
    return redirect('home')

def update(request,keyid):
    if request.method == 'POST':
        taskone = request.POST.get('task',False)
        obj = Todo.objects.get(id=keyid)
        
        print(keyid)
        print(obj)
        obj.task=taskone
        obj.save()
        print(obj.task)
        return redirect('home')
    obj = Todo.objects.get(id=keyid)
    key = keyid
    objs = {
        "obj":obj,
        "key":key
    }
    return render(request,'update.html',objs)

def complete(request,keyid):
    obj = Todo.objects.get(id=keyid)
    obj.complete = True
    obj.save()
    return redirect('home')

def uncomplete(request,keyid):
    obj = Todo.objects.get(id=keyid)
    obj.complete = False
    obj.save()
    return redirect('home')

