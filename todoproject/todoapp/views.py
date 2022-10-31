from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import task
from .forms import TodoForm
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class TaskListview(ListView):
    model=task;
    template_name = 'index.html'
    context_object_name = 'a'
class TaskDetailview(DetailView):
    model=task;
    template_name = 'details.html'
    context_object_name = 'b'
class TaskUpdateview(UpdateView):
    model=task;
    template_name = 'update.html'
    context_object_name = 'b'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('todoapp:classviewdetails',kwargs={'pk':self.object.id})
class TaskDeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:classviewhome')

def add(request):
    a=task.objects.all()
    if request.method =='POST':
        name=request.POST.get('taskname','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        tasks=task(name=name,priority=priority,date=date)
        tasks.save()
    return render(request,"index.html",{'a':a})
def details(request):
    tasks=task.objects.all()
    return render(request,'details.html',{'tasks':tasks})
def delete(request,taskid):
    if request.method=='POST':
        a = task.objects.get ( id=taskid)
        a.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    b=task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=b)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'b':b})




# Create your views here.
