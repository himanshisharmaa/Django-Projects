from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from .models import Link

# Create your views here.
def scrape(request):
    if request.method=="POST":
        
        url=request.POST.get('search','')
        page=requests.get(url)
        soup=BeautifulSoup(page.text,'html.parser')
        link_address=[]
        for link in soup.find_all('a'):
            link_address=link.get('href')
            link_text=link.string
            try:
                 obj = Link.objects.get(address=link_address)
            except Link.DoesNotExist:
                obj = None
            if obj==None:
                Link.objects.create(address=link_address,name=link_text)
        return redirect('/')
    else:
        data=Link.objects.all()

    return render(request,'myapp/result.html',{'data':data})

def delete_all(request):
    Link.objects.all().delete()
    return redirect('/')