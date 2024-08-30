from django.shortcuts import render
from .models import cat,prod

# Create your views here.

def Home(request):
    cat_list = cat.objects.all()
    return render(request,'home.html',context={
        'cat_list':cat_list,
    })
def Info(request,id):
    prod_list = cat.objects.filter(pk=id)
    return render(request,'info.html',context={
        'prod_list':prod_list,
    })