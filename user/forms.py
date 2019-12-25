from django import forms #djangonun form yapıları için geliştirilmiş kutuphanesi

class registerform(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanici Adi") #bunun hata mesajları gibi required gibi özellikleri var bak onlara
    #aslında charfield input type text alanına donusur
    password=forms.CharField(max_length=20,label="Sifre",widget=forms.PasswordInput) # widget degiskeni sıfre tipinde oldugunu bildirmemize yaradı
    confirm = forms.CharField(max_length=20,label="Parolayı dogrular",widget=forms.PasswordInput)

    def clean(self):#bu clean fonksiyonu aynı zamanda form yapısının içinde de vardır biz bastan yazıcaz
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolara Eşleşmiyor")
        # görmüş oldugunun sistemde java script kodu yazmadan sadece python ile web sayfasını gene kontrol edbilirz
        # ve bu yontemle ıstedigim ayarı gene yapabiliriz, istedigimiz valide'ti.
        else: 
            # biz eger bu işlem dogruysa bu alanları sözlk yapısı olarak donmek gerekiyor
            # bunun mantıgını tam olark anla
            values = {
                "username":username,
                "password":password
            }
            return values
            # https://docs.djangoproject.com/en/3.0/ref/forms/ bu adresten daha da detaylı bakabilrsin

class loginform(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanici Adi")
    password = forms.CharField(max_length=20,label="Şifre",widget=forms.PasswordInput)
