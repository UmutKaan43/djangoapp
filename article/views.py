from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib import messages
from .models import Article,comment
from django.contrib.auth.models import User
from .forms import articleForm
from django.contrib.auth.decorators import login_required # uyeliksiz girişi engelleyecek fonk

#httpresponse http cevaplarıdır işte 200 404 ..

# Create your views here.

def index(request): #burada fonksiyonları yazarız urls.py'de bildiririrz,request django sayfadan atılan istek dogrultusunda içine veri atar
#her view fonksiyonunda ilk parametre olark bulunmalı!!!
   # return HttpResponse("<h3>cvc</h3>") bu şekilde cevaplerda donebiliriz  
   context = {
      "numbers":{
         "bir":1,
         "iki":2
     },
      "no2":2
   } # bu şekilde sozluk yapısını dısarıda olusturupda verebiliriz
   return render(request,"index.html",context) #burada ilk paramete olarak o request'i istiyor article/index.html belirtilen klasöorun altında da olabilir



def about(request):
   return render(request,"about.html",{ "number":7}) 
   #aslında djangonun yapısı daha iyi, cunku context.number değil direk number olarak kullanıyoruz hml'de
   # flask'dan farklı olarak context te sözlük yapısı kullanırız sözlük yapılarını context degiskenıne atayıp bunu html'de kullanabilirz

def dashboard(request):
   articles = Article.objects.filter(auther=request.user) # sisteme giriş yapanın makalelerini aldık
   context = {
      "articles":articles
   }
   return render(request,"dashboard.html",context)

@login_required(login_url="user:login") #hem aktarıyor hemde hata veriyor user viewe bak fonksiyonlarına!!!
def addarticle(request): #dosya yukleme açığı var sadece .jgp lere izin ver
   if request.method =="POST":
      form = articleForm(request.POST,request.FILES or None) # files ise gelen dosyalardır
      if form.is_valid():
         #title = form.cleaned_data.get("title")
         #content = form.cleaned_data.get("content")
         #auth = request.user
         #yeni = Article()
         #yeni.title=title
         #yeni.content=content
         #yeni.auther=auth
         #yeni.save()

         #CREATE ile oluştururken neden hata verir düşün onu
         #YUKARIDA İŞLEM YANLIS DEĞİL FAKAT DAHA DA KONTROLLU YAPILABİLİR, ZATEN MODEL'DEN ALDIGIMIZ İÇİN VERİLERİ DİREK SAVE DERSEK
         #SIKINTIIZ KAYIT EDER...
         article = form.save(commit=False) #bu save belirtilen objeyi oluşturup veri tabanına kayıt eder, commit=False yapınca ise sadece tum detayları ile oluşturup kayıt etmeden doner
         article.auther=request.user
         article.save()
         messages.success(request,"Makale başarı ile kayıt edildi")
         return redirect("article:dashboard")
      else:
         messages.error(request,"Makale kayıt edilirken hata oluştu tum alanları doldurunuz") 
         return render(request,"addarticle.html",{"form":form})
   else:
      form = articleForm()
      return render(request,"addarticle.html",{"form":form})


def article(request,id):
   #makale = Article.objects.get(id = id) #yukarıda filter burada get ile aldık bunun sebeblerini araştır
   #get ile find gibi tek obje alırız, ama filter coklu obje liste doner o yuzden yukarıda olmaz burada olur
   #makale = Article.objects.filter(id=id).first() dersen bunuda kullanabilirsin yerine
   makale = get_object_or_404(Article,id=id) # 1. parametre cekecegi model 2. parametre koşul
   # 404 o obje varsa doner yoksa 404 bulunamadı hatası doner, kendisi içinde otomatik doner

   comments = makale.comments.all() # related_name="comments" 'den dolayı guzelcene cagırmıs olduk
   return render(request,"article.html",{"makale":makale,"comments":comments}) #o sayfa varsa doner yoksa 404 doner

@login_required(login_url="user:login")
def update(request,id):
   makale = get_object_or_404(Article,id=id) #buönemli kullan bunu surekli eğer o article yoksa 404 doner
   form = articleForm(request.POST or None,request.FILES or None,instance=makale)
   #instace ile verince belki valid kontrol edilmiyor olabilir oyle olunca cok onemli degil
   # burada makale yi instance objesine gonderirsen bunun içine o veriler yazılır
   if form.is_valid():
      article = form.save(commit=False)
      article.auther = request.user
      article.save()
      messages.success(request,"başarı ile kayıt edildi")
      return redirect("article:dashboard")
   
   return render(request,"update.html",{"makale":makale,"form":form})

@login_required(login_url="user:login")
def delete(request,id):
     mak = get_object_or_404(Article,id=id)
     Article.delete(mak)
     # guncelleme komutunu kullanmıyoruz
     messages.success(request,"Makale başarı ile silindi")
     return redirect("article:dashboard") # article uygulamasının altında dashboarda'a git dedik

def articles(request):
   if "obje" in request.GET:
      ara = request.GET["obje"] #bu sekilde verileri get ile alabiliriz, request.GET.get("obje") ile'de kolayca alabilirsin bunu kullanırsan bu eğer null ise hata vermez
      makas = Article.objects.filter(title__contains=ara)
      makas2 =Article.objects.filter(content__contains=ara)
      makas3 = User.objects.filter(username__contains=ara).first() # username'den arama yaptık 
      li = []
      if makas3:
         makas4 = Article.objects.filter(auther=makas3)# user'indan sunu unutma artık veri tabanıyla işimiz yok modellerle işimiz var
         li = [makas,makas2,makas4]
      else:
         li = [makas,makas2]
      don =[] # listeleri bilestiremeyince yeni liste donduk
      for i in li:
         if len(i)!=0:
            for x in i:
               k = False
               for p in don:
                  if x.id == p.id:
                     k=True
               if k:
                  continue
               else:                               
                  don.append(x)
      return render(request,"articles.html",{"ARK":don})
   articlesx = Article.objects.all()
   return render(request,"articles.html",{"ARK":articlesx})

def Addcomment(request,id):
   art = get_object_or_404(Article,id=id) # yaptıgım null işlemini kendisi yapıyor sende deneyebilirsin yapabilrsin diger frameworklerde
   if request.method == "POST":
      comment_auther = request.POST.get("comment_auther")
      comment_content = request.POST.get("comment_content")
      yorum = comment(article=art,comment_auther=comment_auther,comment_content=comment_content)
      #yorum.article=art boylede verebilirsin.
      yorum.save()
   return redirect(reverse("article:article",kwargs={"id":id})) # dorek url yazıpda donebiliriz, "/Articles/article/"+str(id)
   # bildigimiz redictToaction'in aynısı oldu reverse ile istersek parametre'de gonderebiliriz, daha dinamik bir siste moldu
   # get olsada post olsda article sayfası gozuksun dedik
