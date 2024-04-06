from django.shortcuts import render,redirect
from .models import *
from studioapp.forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from studioapp.forms import OrderForm
from .forms import OrderForm


def home(request):
    cat_pro = Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"cat_pro": cat_pro})

from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.http import HttpResponse
from django.shortcuts import render
from .models import Order

    
def place_order(request):
    if request.method == 'POST':
        First_name = request.POST.get('First_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        address = request.POST.get('address', '')

        
        order = Order(
            First_name=First_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address
        )
        order.save()
        messages.success(request, 'Your order has been placed successfully!')
        return redirect('thanks_you_page')
       
        
        
    return render(request, 'shop/place_order.html')

   
    

def thanks_you_page(request):
    return render(request, 'shop/thank_you.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully")
    return redirect("/")    
        

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:   
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password")
                return redirect("/login")
        return render(request,"shop/login.html")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Registeration is success you can Login Now..!")
            return redirect('/login')
    return render(request,"shop/register.html",{'form':form})

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"shop/collections.html",{"catagory":catagory})

def collections_view(request, name):
    catagory_name = slugify(name).replace('-', ' ')

    try:
        catagory = Catagory.objects.get(name=catagory_name, status=0)
        cat_pro = Product.objects.filter(Catagory=catagory)
        return render(request, "shop/categoryproduct/home.html", {"cat_pro": cat_pro,"cat_name":catagory_name})
    except Catagory.DoesNotExist:
        messages.warning(request, "No such catagory found")
        return redirect('collections')
def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/categoryproduct/product_details.html', {'product': product})
    
    
def about(request):
    return render(request,'shop/inc/aboutas.html')

