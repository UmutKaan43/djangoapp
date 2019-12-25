from django.db import models
from ckeditor.fields import RichTextField # ckeditor için 
# Create your models here.
class Article(models.Model): # aynı orm'daki gibi db.model fakat bu sefer django db model oldu
    auther = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar") #burada dedik ki bu yabancıl anahtar atanacak ve belirttiğimiz tablodan bir yabancıl anahtar alıcak edik
    # aynı zamanda yukarıda user'ı bagladıgımız için hazır olarak user sayfası oluşucak
    #Models.CASCADE --> eger user silinirse ona ait olan bu verilerde silinsin dedik
    #verbose_name = sayfalarda bu isim ile gorulur bu değişkenler
    title = models.CharField(max_length=50,verbose_name="Başlık") #hem veri tabanı olusturacak hemde burada wtform'daki gibi form yapıları oluşturuyoruz
    #content = models.TextField(verbose_name="İçerik") # texxtfield textarea gibi charfield sınırlı zaten yukarıda max kelimeyi verdik
    content = RichTextField() # ckedior için
    article_img = models.FileField(blank=True,null=True,verbose_name="Makaleye fotoraf ekleyin:") #blank bu alan boş olabilir, ve null olablir dedik
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi") #veri tabanı için o an, biz bunu vermicez o anki tarihi otomatik olarak atıcak

    def __str__(self):
        return self.title # bu fonk bildigin üzere auther'ın adını yazdırınca cıkan yazıyı yazar ( print(auther) )
        #buraya istediğimiz değeri dondurebiliriz, bunu yapma amacımı admin sayfasında
        #article object yazısını gordugumuzden onun yerine bunu işaretledik
    class Meta:
        ordering = ['-created_date'] # en son eklenen ilk gösterilir - koyarsak, içine degisken tablo adı alır

class comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments") # yabancıl anahtar verirken dogrudan class'ı da verebiliriz
    #related_name article.comments diyerek article tablosundan comment tablosuna ulasmamızı saglar
    comment_auther = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True,verbose_name="Yazma Tarihi")

    def __str__(self):
        return self.comment_auther+" ' "+self.article.title+" ' bloguna yorum yazmiş."
    class Meta:
        ordering = ['-comment_date']