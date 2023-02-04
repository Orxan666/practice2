from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method=='GET':
        return render(request,'contact.html')
    elif request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

def confirm_contact(request):
    if(reqeust.method)=='GET':
        return redirect('info:contact')