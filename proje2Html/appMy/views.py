from django.shortcuts import render, redirect 
from appMy.models import *
from django.db.models import Q
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout





# Create your views here.

def indexPage(request):
    blog_list = Blog.objects.all()
    context={
        "blog_list":blog_list,
    }
    return render(request, 'index.html', context)

def aboutPage(request):
    context = {}
    return render(request,"about.html",context)


def contactPage(request):
    if request.method == "POST":
        fname = request.POST.get("fullname")
        email = request.POST.get("email")
        text = request.POST.get("textis")
        img = request.POST.get("file")
        
        contact = Contact(fullname=fname, email=email, text=text , img=img) 
        contact.save()
        return redirect("contactPage")  

    def __str__(self):
        return self.img
    
    
    context = {}
    return render(request,"contact.html",context)


def categoryPage(request):
    blog_list=Blog.objects.all()
    context ={
        "blog_list":blog_list,
    }
    return render(request,"category.html",context)

#user
def loginPage(request):
    hata = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:
            
            user = authenticate(username=username , password=password)
            if user:
                login(request,user)
                
                return redirect("indexPage")
            else:
                hata = "Kullanıcı Adı veya şifre yanlış !"  
    
    context = {
        "hata":hata,
    }
    return render(request,'user/login.html', context)
    
    
    

def registerPage(request): 
    
    if request.method == "POST":
        
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    
                   user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password1)
                   user.save()
                   return redirect("loginPage")   
                   
                    
    context = {}
    return render(request, 'user/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect("loginPage")