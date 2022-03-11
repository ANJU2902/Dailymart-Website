from django.shortcuts import render,redirect
from django.http import HttpResponse
from dailymartapp. models import*
from shopapp.models import cartdb, checkoutdb,contactdb, registerdb
from django.db.models.aggregates import Sum
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def shop(request):
    data=categorydb.objects.all()
    return render(request,'index2.html',{'data':data})

def contact(request):
    return render(request,'contact.html')

def getone(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data=contactdb(name=name,phone=phone,email=email,subject=subject,message=message)
        data.save()
    return redirect('shop')

def message(request):
    data=contactdb.objects.all()
    return render(request,'messages.html',{'data':data})

def register(request):
    return render(request,'registration.html')

def regi(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        username=request.POST.get('username')
        password=request.POST.get('password')
        data=registerdb(name=name,email=email,phone=phone,username=username,password=password)
        data.save()
    return redirect('shop')

def registrations(request):
    data=registerdb.objects.all()
    return render(request,'registrations.html',{'data':data})

def userlogin(request):
    return render(request,'userlogin.html')


def userin(request):
    if request.method=="POST":
        username_a=request.POST.get('username')
        password_a=request.POST.get('password')
        print(password_a)
        print(username_a)
        if registerdb.objects.filter(username=username_a,password=password_a).exists():
            data=registerdb.objects.filter(username=username_a,password=password_a).values('name','email','phone','id').first()
            request.session['name']=data['name']
            request.session['email']=data['email']
            request.session['phone']=data['phone']
            request.session['username']=username_a
            request.session['password']= password_a
            request.session['id']=data['id']
            return redirect('shop')
        else:
            return render(request,'userlogin.html',{'msg':"sorry... invalid username or password"})
    else:
        return redirect('userlogin')
        
def logout(request):
    del request.session['name']
    del request.session['email']
    del request.session['username']
    del request.session['password']
    del request.session['id']
    return redirect('shop')

def vegetables(request):
    return render(request,'vegetables.html')

def fruits(request):
    return render(request,'fruits.html')

def product(request,cat):
    if(cat=="all"):
        data=productdb.objects.all()
    else:
        data = productdb.objects.filter(category=cat)
    return render(request,'products.html',{'data':data})

def single(request,pid):
    data=productdb.objects.filter(id=pid)
    return render(request,'single.html',{'data':data})

def cart(request):
    u = request.session.get('id')
    data=cartdb.objects.filter(userid=u,status=0)
    total=cartdb.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'cart.html',{'data':data,'total':total})

def check(request):
    u = request.session.get('id')
    data=cartdb.objects.filter(userid=u,status=0)
    total = cartdb.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'check.html',{'data':data,'total':total})
    
def cart1(request,pid):
    if request.method=="POST":
        userid=request.POST.get('userid')
        total=request.POST.get('total')
        quantity=request.POST.get('quantity')
        print(userid)
        data=cartdb(productid=productdb.objects.get(id=pid),userid=registerdb.objects.get(id=userid),total=total,quantity=quantity,status=0)
        data.save()
    return redirect('cart')

def deletec(request,cid):
    cartdb.objects.get(id=cid).delete()
    return redirect('cart')

def checkout(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        u = request.session.get('id')
        order = cartdb.objects.filter(userid=u,status=0)
        for i in order:
            data = checkoutdb(cartid=cartdb.objects.get(id=i.id),name=name,email=email,mobile=mobile,address=address)
            data.save()
            cartdb.objects.filter(id=i.id).update(status=1)
        return redirect('shop')


@csrf_exempt
def cart_update(request):
    if request.method == "POST":
        cartid = request.POST.get('pid')
        q = request.POST.get('qty')
        print(q)
        p = request.POST.get('price')
        tot = float(q)*float(p)
        print(tot)
        cartdb.objects.filter(id=cartid).update(total=tot,quantity=q)
    return HttpResponse()



