"""my_first_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

def home_page(request):
    response = render(request, 'index.html')
    return HttpResponse(response)

def portfolio(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))

    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me(request):
    context = {
        'skills': ['Dependable', 'Problem solving', 'Persistent', 'Creative'],
        'interests': ['Fitness', 'Eating', 'Gunpla', 'You ;)']
    }
    response = render(request, 'about_me.html', context)
    return HttpResponse(response)

def favourites(request):
    context = {
        'fave_links': {'Bitmaker':'https://bitmaker.co/',
        'Bitmaker Web Developement': 'https://bitmaker.co/courses/web-development',
        'LMGTFY':'https://lmgtfy.com/'}
    }
    response = render(request, 'favourites.html', context)
    return HttpResponse(response)

urlpatterns = [
path('home/', home_page),
path('portfolio/', portfolio),
path('about_me/', about_me),
path('favourites/', favourites)
]
