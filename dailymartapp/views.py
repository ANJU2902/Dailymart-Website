from django.shortcuts import render,redirect
from django. http import HttpResponse

from shopapp.models import cartdb, checkoutdb, contactdb, registerdb
from. models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    ucount=categorydb.objects.all().count()
    ucount1=productdb.objects.all().count()
    ucount2=registerdb.objects.all().count()
    ucount3=contactdb.objects.all().count()
    ucount4=checkoutdb.objects.all().count()
    return render(request,'index.html',{'ucount':ucount,'ucount1':ucount1,'ucount2':ucount2,'ucount3':ucount3,'ucount4':ucount})
    
def category(request):
    return render(request,'add_category.html')

def view(request):
    data=categorydb.objects.all()
    return render(request,'view_category.html',{'data':data})

def getdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        image=request.FILES['photo']
        data=categorydb(name=name,description=description,photo=image)
        data.save()
        return redirect('view')

def edit(request,sid):
    data=categorydb.objects.filter(id=sid)
    return render(request,'edit.html',{'data':data})
    
def delete(request,vid):
    categorydb.objects.get(id=vid).delete()
    return redirect('view')

def update(request,wid):
    if request.method=='POST':
        name_c=request.POST.get('name')
        description_c=request.POST.get('description')
        try:
            image_r=request.FILES['file']
            fs = FileSystemStorage() 
            file = fs.save(image_r.name, image_r)
        except MultiValueDictKeyError :
            file=categorydb.objects.get(id=wid).photo
        
        categorydb.objects.filter(id=wid).update(name=name_c,description=description_c,photo=file)
    return redirect('view')

def addpro(request):
    data=categorydb.objects.all()
    return render(request,'add_product.html',{'data':data})

def p_view(request):
    data=productdb.objects.all()
    return render(request,'view_product.html',{'data':data})

def getpro(request):
    if request.method=="POST":
        pname=request.POST.get('pname')
        category=request.POST.get('category')
        weight=request.POST.get('weight')
        price=request.POST.get('price')
        image=request.FILES['photo']
        data=productdb(pname=pname,category=category,weight=weight,price=price,photo=image)
        data.save()
        return redirect('p_view')

def pedit(request,mart1):
    data=productdb.objects.filter(id=mart1)
    data1 = categorydb.objects.all()
    return render(request,'pedit.html',{'data':data,'data1':data1})

def pdel(request,mart2):
    data = productdb.objects.get(id=mart2).delete()
    return redirect('p_view')



def update1(request,mart3):
    if request.method=='POST':
        pname_c=request.POST.get('pname')
        category_c=request.POST.get('category')
        weight_c=request.POST.get('weight')
        price_c=request.POST.get('price')
        try:
            image=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=mart3).photo
        productdb.objects.filter(id=mart3).update(pname=pname_c,weight=weight_c,category=category_c,price=price_c,photo=file)
        return redirect('p_view')
        
def adminlogin(request):
    return render(request,'adminlogin.html')

def adlogin(request):
    username_a = request.POST.get('username')
    password_a = request.POST.get('password')
    if User.objects.filter(username__contains=username_a).exists():
        user = authenticate(username=username_a,password=password_a)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('index')
        else:
            return render(request,'adminlogin.html',{'msg':"Sorry... Invalid username or password"})
    else:
        return redirect('adminlogin')

def order(request):
    data=checkoutdb.objects.all()
    return render(request,'order.html',{'data':data})

def getorder(request):
    if request.method=="POST":
        cartid_c=request.POST.get('cartid')
        name_c=request.POST.get('name')
        email_c=request.POST.get('email')
        mobile_c=request.POST.get('mobile')
        address_c=request.POST.get('address')
        data=checkoutdb(cartid=cartid_c,name=name_c,email=email_c,mobile=mobile_c,address=address_c)
        data.save()
        return redirect('order')



