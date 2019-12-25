# bu url sayfası article sayfasına ait alt sayfaların baglanti linkleri olucak, article/deneme1 şeklinde olanlar için

from django.contrib import admin
from django.urls import path
from . import views # şuanki klasöromuzdeki demek o .

app_name = "article" # ileride redict işlemı yaparken bu isim lazım olcek

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addarticle,name="addarticle"),
    path('article/<int:id>',views.article,name="article"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('',views.articles,name="articles"),
    path('comment/<int:id>',views.Addcomment,name="comment"),
]