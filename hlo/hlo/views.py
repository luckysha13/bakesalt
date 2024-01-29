from django.http import HttpResponse
from django.shortcuts import render
from hii.models import log

def login(request):
    if request.method=="POST":
        name=request.POST.get('Username')
        pas=request.POST.get('Password')

        ab=log(Username=name,Password=pas)
        ab.save()
    return render(request,'pg1.html')

def save_login(request):
    pass
    return render(request,'pg1.html')

def pra(request):
    data={
        'title':'practice page',
        'clist':['saler','customer'],
        'stud_details':[
            {'name':'vishal','phone': 8901237890},
            {'name':'grishma','phone':8905245671}
        ]
    }
    return render(request,'practice.html',data)

def home(request):
    return HttpResponse("Welcome to home page")

def about(request):
    return HttpResponse("Welcome to about us page")

def details(request,id):
    return HttpResponse(id)




