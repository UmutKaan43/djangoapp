from django.shortcuts import render,redirect,HttpResponse
from .forms import registerform,loginform

from django.contrib.auth.models import User
from django.contrib import messages # flash mesajlarını gondermek için
from django.contrib.auth import login,authenticate,logout
 #bu fonksiyonun içine user veririz ve o kişi artık login olur, authenticate user name passworde gore varsa diye bakıcak

def boyut(item):
    y=0
    for i in item:
        y+=1
    return y

def next_ayir(nex):
    yeni = ""
    ln = boyut(nex)
    for i in nex:       
        if(i=="/"):
            yeni+=":"
        else:
            yeni+=i
    yeni=yeni[1:ln]
    yeni=yeni[0:ln-2]
    x = yeni.split(":")
    if(x[0]=="Articles"):
        x[0]="article"
    don = ""
    vc=0
    by = boyut(x)-1
    for i in x:       
        if(vc==by):
            don+=i   
            break
        else:
            don+=i+":"
            
        vc+=1
    return don


def loginUser(request): # giriş yapınca tekrar bu sayfaya baglanmaya calısırsa baglanamasın
    if request.method=="POST":
        form = loginform(request.POST)
        if form.is_valid(): # assagıdsa cleaned data verileri kullanmak için clean fonk'unu calıstırmamız gerek burada onu yaptık
            username= form.cleaned_data.get("username") # dikkatini ver !!!!!!
            password = form.cleaned_data.get("password")
            #kisi = User.objects.get(username=username) bu yontemlede belki alanılabilir ama password şifreli
            uss = authenticate(username=username,password=password)
            if uss!=None: #burada içine aldıgı creantials değişkeni belki degisken alabilen bir kwarg yapısıdır
                messages.success(request,"Başarı ile giriş yaptınız")
                login(request,uss)
                if "next" in request.GET:
                    vs = request.GET["next"]
                    don = next_ayir(vs)
                    return redirect(don)
                else:
                    return redirect("index")
            else:
                messages.error(request,"Kullanıcı Adı Yada şifre hatalı")
                context = {
                "form":form
                }
                return render(request,"login.html",context)

        else:
            messages.error(request,"Girişini için eksik bilgi var")
            context = {
                "form":form
            }
            return render(request,"login.html",context)
    else:
        if "next" in request.GET:
            messages.error(request,"Bu sayfayı görebilmek için giriş yapmalısınız ..")
        form = loginform()
        context = {
            "form":form
        }
        return render(request,"login.html",context)
def register(request):
    form = registerform(request.POST or None) 
    if request.method =="GET":
        form = registerform()
        context = {
            "form":form
            }
        return render(request,"register.html",context)
    if form.is_valid(): 
        username= form.cleaned_data.get("username")
        password= form.cleaned_data.get("password")
        newus = User(username = username)
        newus.set_password(password)
        newus.save()
        login(request,newus)
        messages.success(request,"Başarıyla kayıt oldunuz") # django mesajları debug,info,warning,success,eror seklinde 5 tiptir tabi ekleyebilirz
        return redirect("index") 
    else: #bu yapı için else yapısını kullanmadan dogrudan ekleme yap
        messages.error(request,"Kaydınız gerçekleştirilemedi")
        form = registerform(request.POST)
        return render(request,"register.html",{"form":form})
    
def logoutUser(request):
    logout(request)
    messages.success(request,'sistemden çıkış yaptınız..')
    return redirect("index")