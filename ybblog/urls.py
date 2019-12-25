"""ybblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings #ayarlar dosyası gibi bişi, django
from django.conf.urls.static import static #buda belirtilen yere python dosyalarından erişmemiz için gerkli fonk


from article import views 
#bu dosya url adreslerimiz veridğimiz zaman çalısık olan fonksiyonu yazar
#assagıda hazır gelen admin sayfsaını goruyorsun bunun gibi tum url leri fonksiyonarla ozleştırıcez

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"), # / koyarsan django hata verir redirect işlemi için isim verdik
    path("about/",views.about,name="about"), #buradaki basit detay şudur ki link bildirimi about/ şekilndeo lur
   # path("details/<int:id>",views.details,name="details") # id dinamil url aldık
   path("Articles/",include("article.urls")), # eğer articles kalıbınında bir değer gelirse sen articles'in altındaki urls e git dedik
   path("User/",include("user.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)