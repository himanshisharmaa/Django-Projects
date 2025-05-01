from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    products=Product.objects.all()

    return render(request,'myapp/index.html',{'products': products})


def detail_view(request,id):
    product=Product.objects.get(id=id)
    return render(request,'myapp/detail.html',{'product':product})

@login_required
def create_product(request):
    if request.method=="POST":
        product_form=ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            new_product=product_form.save(commit=False)
            new_product.seller=request.user
            new_product.save()
            return redirect('/')
    product_form=ProductForm()
    return render(request,'myapp/create_product.html',{'product_form':product_form})

@login_required
def product_edit(request,id):
    product=Product.objects.get(id=id)  
    if product.seller != request.user:
        return redirect('invalid')  
    product_form =ProductForm(request.POST or None , request.FILES or None,instance=product)
    if request.method=="POST":
        if product_form.is_valid():
            product.save()
            return redirect('/dashboard/')
    return render(request,'myapp/product_edit.html',{'product_form':product_form,'product':product})

@login_required
def product_delete(request,id):
    product=Product.objects.get(id=id)  
    if product.seller != request.user:
        return redirect('invalid') 
    if request.method=="POST":
        product.delete()
        return redirect('/dashboard/')
    return render(request,"myapp/delete.html",{'product':product})

@login_required
def dashboard(request):
    products=Product.objects.filter(seller=request.user)
    return render(request,'myapp/dashboard.html',{'products':products})

def register(request):
    if request.method=="POST":
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return redirect('/')
        
    register_form=UserRegistrationForm()
    return render(request,'myapp/register.html',{'register_form':register_form})

def invalid(request):
    return render(request,'myapp/invalid.html')

# def my_purchases(request):
#     orders = OrderDetail.objects.filter(customer_email=request.user.email)
#     return render(request, 'myapp/purchases.html',{'orders':orders})