from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Vegitables


# Create your views here.
def Index(request):
    data=Vegitables.objects.all()
    details={'details':data}
    if request.method=='POST':
        item_id=request.POST.get('item_id')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(item_id)
            if quantity:
                cart[item_id]=quantity+1
            else:
                cart[item_id]=1
            
        else:
            cart={}
            cart[item_id]=1
        request.session['cart']=cart
       
     
    return render(request,'index.html',details)
def Contact(request):
    return render(request,'contact.html')
def Register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirm_password')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,'successfully created')
                return redirect('login')          
        else:
            messages.info(request,'password do not matched')
            return redirect('register')


        
    else:
        return render(request,'register.html') 

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'username and password cannot exist')
            return redirect('login')


    return render(request,'login.html')
def Cart(request):
    
    ids=list(request.session.get('cart').keys())
    datas=Vegitables.objects.filter(id__in=ids)
    details={'details':datas}

    return render(request,'cart.html',details)

    
    
    

