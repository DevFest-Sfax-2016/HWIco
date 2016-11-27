from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Post

from django.http import HttpResponse

def index(request):
    return render(request, 'firstapp/index.html')
    #liaison entre index et view pour afficher e contenu de index ds le navigateur
def about_us(request):
    return render(request, 'firstapp/full_width.html')

def contact(request):
    return render(request, 'firstapp/contact.html')

def question(request):
    return render(request, 'firstapp/questionnaire.html')

def form(request):
    return render(request, 'firstapp/01.html')

#def index2(request):
#   return render(request, 'firstapp/index2.html')
#def acceuil(request):
#    return render(request, 'firstapp/acceuil.html')
#def contact(request):
#    return render(request, 'firstapp/contact.html')


#class PostDetail(DetailView):
#    model = Post