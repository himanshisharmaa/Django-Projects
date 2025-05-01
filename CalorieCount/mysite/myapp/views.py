from django.shortcuts import render,redirect
from .models import Food,Consume

# Create your views here.
def index(request):
    if request.method=="POST":
        food_consumed=request.POST.get('food_consumed')
        consumed=Food.objects.get(name=food_consumed)
        user=request.user
        consume=Consume(user=user,food_consumed=consumed)
        consume.save()
        foods=Food.objects.all()
    else:
        foods=Food.objects.all()
    consumed_by_user=Consume.objects.filter(user=request.user)
    return render(request,'myapp/index.html',{'foods':foods,'consumed':consumed_by_user})

def delete_item(request,id):
    instance=Consume.objects.get(id=id)
    if request.method=="POST":
        instance.delete()
        return redirect('/')   
    return render(request,"myapp/delete.html")