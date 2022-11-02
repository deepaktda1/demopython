from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import movie
from .forms import MovieForm


# Create your views here.
def reg(request):
    movies=movie.objects.all()
    return render(request,'index.html',{'a':movies})

def detail(request,movie_id):
    x=movie.objects.get(id=movie_id)
    return render(request,"details.html",{'b':x})
def movie_add(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        des = request.POST.get('des',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        x=movie(name=name,des=des,year=year,img=img)
        x.save()
    return render(request,'add.html')

def update(request,id):
    y=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=y)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'y':y})
def delete(request,id):
    if request.method=="POST":
        y=movie.objects.get(id=id)
        y.delete()
        return redirect('/')
    return render(request,'delete.html')

