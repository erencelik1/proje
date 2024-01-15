from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(("İşler"),max_length=50)
    text = models.TextField()
    date_now = models.DateTimeField(("Tarih - Saat"), auto_now=False, auto_now_add=False)
    author = models.CharField(("Yazar"), max_length=50)
    
class Contact(models.Model):
    fullname = models.CharField(("Ad Soyad"), max_length=50) 
    email = models.EmailField(("Email"), max_length=254)
    text = models.TextField(("İletişim Yazısı")) 
    img =models.FileField(("CVLER"))