from django.shortcuts import render
from .models import Products,Order
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    products=Products.objects.all()
    search=request.GET.get('item_name')
    if search!='' and search is not None:
        products=Products.objects.filter(title__icontains=search)
    paginator=Paginator(products,4)
    page=request.GET.get('page')
    products=paginator.get_page(page)
    return render(request,'shop/index.html',{'products':products})

def detail(request,id):
    product_object=Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})

def checkout(request):
    if request.method=="POST":
        items=request.POST.get('items',"")
        total=request.POST.get('total',"")
        name=request.POST.get('name',"")
        mail=request.POST.get('mail',"")
        address=request.POST.get('address',"")
        city=request.POST.get('city',"")
        state=request.POST.get('state',"")
        zipcode=request.POST.get('zipcode',"")
        order=Order(items=items,
                    name=name,
                    mail=mail,
                    address=address,
                    city=city,
                    state=state,
                    zipcode=zipcode,
                    total=total
                    )
        order.save()
        print("Order Saved")

    return render(request,'shop/checkout.html')