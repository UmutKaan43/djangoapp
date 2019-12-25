from django import forms
from .models import Article
#Modelfrom yapısı aslında html sayfalarında olusturucagımız form yapıları için oluştrudgumuz classları
#kod tekrarına dusmeden veri tabanı için olusturdugumuz model yapısından dahil edicez..
# bunu yaparken Modelform sınıfını kllanarak meta.modeline özelliklerini alıcagımız sınıfı verdik

class articleForm(forms.ModelForm):
    class Meta:
        model = Article #aslında admin sayfasında oldugu gibi modelini soylmış olduk
        fields = ['title', 'content','article_img'] # içinde hali hazırda alanlar olabilir id gibi yazar gibi onların alınmaması için hangi alanlar 
        #alınacaksa onları yazdık
