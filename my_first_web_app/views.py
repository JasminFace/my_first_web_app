from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('/home')

def gallery(request):
    return HttpResponseRedirect('/portfolio')

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
        'interests': ['Fitness', 'Food', 'Gunpla', 'You ;)']
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