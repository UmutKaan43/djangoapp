from django.contrib import admin

from .models import Article,comment # burada dedikki içindeki dizinde (.) models'in içinden Article'yi çek dedik
#admin.site.register(Article) # buradada Article'yi admin sayfasında göstermiş olduk
# Register your models here.


#bunu yapma amacımız her admin sayfası bir class yapısı  üzerinden işliyor
#bizde o classını kendi işlerimize uygun bir şekilde yazıcaz ModelAdmin 'den turemesi gerek
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin): # burada anlayıcagın üzere decoratırlerı classlar ile de kullanabiliriz bunu daha detaylı araştır
    list_display = ["title","auther","created_date"] #sayfanın ana sayfasında gelen tabloda yazılacak verilerdir.
    list_display_links=["title"] #buraya basılınca duzenlemeye gider istediklerini verebilirsin
    search_fields=["title"] # arama özelliği ekledik içindeki parametler ise sadece o değişkende arama yapar
    list_filter=["created_date"] # içine verilen değişkene gore filitre özelliği verir
    class Meta:
        model = Article # bunu yazma sebebimiz ArticleAdmin aslında article sayfasının modeli oldugunu soyledik,
        # turetmiş oldugmuz ModelAdmin turetildigi sınıfa bakarak içinde meta sınıfını arar ve onun içindeki model değişkenini
        # sayfa bilgisi olarak kullanır istersen baska sayfanın adresini ve onun için kullanır
        # bu yontemle daha da özelleştirme yapabilirz
        # Meta özel isim olarak dogrudan ModelAdmin Metayı arar ondan veri alır başka isim veremessin

admin.site.register(comment)