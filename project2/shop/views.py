from django.shortcuts import render,redirect
from .models import mobile
from .forms import mobileform
# Create your views here.
def shopreg(request):
    mob=mobile.objects.all()
    return render(request,'shopindex.html',{'mob':mob})
def mob_add(request):
    if request.method == 'POST':
        mobname=request.POST.get('mobname',)
        des = request.POST.get('des',)
        price = request.POST.get('price',)
        img = request.FILES['img']
        x=mobile(mobname=mobname,des=des,price=price,img=img)
        x.save()
    return render(request,'mobadd.html')
def mobdetail(request,mobid):
    x=mobile.objects.get(id=mobid)
    return render(request,"mobdetails.html",{'b':x})
def update(request,id):
    c = mobile.objects.get (id=id)
    if request.method == "POST":
      form =mobileform(request.POST,request.FILES,instance=c)
      if form.is_valid():
        form.save()
        return redirect ('/' )
    return render(request,'shopindex.html',{'c':c})
def edit(request,id):
    y = mobile.objects.get(id=id)
    form=mobileform(instance=y)
    return render(request,'update1.html',{'form':form,'y':y})


