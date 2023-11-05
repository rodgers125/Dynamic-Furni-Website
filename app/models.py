from django.db import models


# Create your models here.



class User(models.Model):
    country = models.CharField(max_length=100, blank=False)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)
    company = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    zip = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.lname


class Hero(models.Model):
    text1 = models.CharField(max_length=100, blank=False)
    text2 = models.CharField(max_length=100, blank=False)
    text3 = models.CharField(max_length=100, blank=False)
    text4 = models.CharField(max_length=100, blank=False)
    text5 = models.CharField(max_length=100, blank=False)
    hero_image = models.ImageField(upload_to='images', default='profile.png')

    def __str__(self):
        return self.text1

class Home(models.Model):
    crafted = models.CharField(max_length=100, blank=False)
    crafted_des = models.CharField(max_length=100, blank=False)


    def __str__(self):
        return self.crafted

class Shop(models.Model):
    title_shop = models.CharField(max_length=100, blank=False)
    shop_description = models.CharField(max_length=100, blank=False)

    shop_image1 = models.ImageField(upload_to='images', default='profile.png')
    image1name = models.CharField(max_length=100, blank=False)
    image1price = models.CharField(max_length=100, blank=False)

    shop_image2 = models.ImageField(upload_to='images', default='profile.png')
    image2name = models.CharField(max_length=100, blank=False)
    image2price = models.CharField(max_length=100, blank=False)

    shop_image3 = models.ImageField(upload_to='images', default='profile.png')
    image3name = models.CharField(max_length=100, blank=False)
    image3price = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title_shop
class About(models.Model):
    about_title = models.CharField(max_length=100, blank=False)


    def __str__(self):
        return self.about_title
class Services(models.Model):
    services_title = models.CharField(max_length=100, blank=False)



    def __str__(self):
        return self.services_title
class Blog(models.Model):
    blog_title = models.CharField(max_length=100, blank=False)



    def __str__(self):
        return self.blog_title

class Contact(models.Model):
    contact_title = models.CharField(max_length=100, blank=False)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    message = models.TextField()
