from django.shortcuts import render

from app.models import Hero, Shop, About, Services, Contact, Blog, Home


# Create your views here.

def index(request):
    hero = Hero.objects.first()  # Retrieve the first Hero object
    home = Home.objects.first()
    shop = Shop.objects.first()
    hero_data = {
        'text1': hero.text1,
        'text2': hero.text2,
        'text3': hero.text3,
        'text4': hero.text4,
        'text5': hero.text5,
        'couch': hero.hero_image.url,
        'crafted': home.crafted,
        'crafteddes': home.crafted_des,
        'chair1': shop.shop_image1.url,
        'chair1name': shop.image1name,
        'chair1price': shop.image1price,
        'chair2': shop.shop_image2.url,
        'chair2name': shop.image2name,
        'chair2price': shop.image2price,
        'chair3': shop.shop_image3.url,
        'chair3name': shop.image3name,
        'chair3price': shop.image3price,
    }
    return render(request, 'index.html', {'hero': hero_data})


def about(request):
    hero = Hero.objects.first()  # Retrieve a Hero object
    about = About.objects.first()
    aboutdata = {
        'abouttitle': about.about_title,
        'aboutdes': hero.text3,
        'btn1text': hero.text4,
        'btn2text': hero.text5,
        'couch': hero.hero_image.url,

        'nav': 'about'
    }
    return render(request, 'about.html', {'about': aboutdata})

def blog(request):
    hero = Hero.objects.first()  # Retrieve a Hero object
    blog = Blog.objects.first()
    blogdata = {
        'blogtitle': blog.blog_title,
        'blogdes': hero.text3,
        'btn1text': hero.text4,
        'btn2text': hero.text5,
        'couch': hero.hero_image.url,

        'nav': 'contact'
    }
    return render(request, 'blog.html', {'blog': blogdata})


def cart(request):
    return render(request, 'cart.html', {'nav': 'cart'})


def checkout(request):
    return render(request, 'checkout.html', {'nav': 'checkout'})


def contact(request):
    hero = Hero.objects.first()  # Retrieve a Hero object
    contacts = Contact.objects.first()
    contactsdata = {
        'contacttitle': contacts.contact_title,
        'contactdes': hero.text3,
        'btn1text': hero.text4,
        'btn2text': hero.text5,
        'couch': hero.hero_image.url,

        'nav': 'contact'
    }
    return render(request, 'contact.html', {'contact': contactsdata})


def services(request):
    hero = Hero.objects.first()  # Retrieve a Hero object
    service = Services.objects.first()
    servicesdata = {
        'servicestitle': service.services_title,
        'servicesdes': hero.text3,
        'btn1text': hero.text4,
        'btn2text': hero.text5,
        'couch': hero.hero_image.url,

        'nav': 'services'
    }
    return render(request, 'services.html', {'services': servicesdata})


def shop(request):
    shop = Shop.objects.first()  # Retrieve the first Hero object
    hero = Hero.objects.first()
    shop_data = {
        'shop_title': shop.title_shop,
        'shop_des': shop.shop_description,
        'couch': hero.hero_image.url,

    }
    return render(request, 'shop.html', {'shop_data': shop_data})


def thankyou(request):
    return render(request, 'thankyou.html', {'nav': 'thankyou'})
