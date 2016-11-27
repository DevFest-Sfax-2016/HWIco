from django.conf.urls import  url
from.views import * #,PostDetail,acceuil,index2
#from app.views import index


urlpatterns = [
   # url(r'^$',PostList.as_view()),
    url('^$',index, name='index'),
    url('^about_us/?$', about_us, name='about_us'),
    url('^contact/?$', contact, name='contact'),
    url('^form/?$', form, name='form'),
    url('^question/?$', question, name='question'),
    #^ et $ ----> ne pas ajouter des symb dans le lien sinn error
                               #? aprés qq chose optionelle
                               #r enlever l'effet de /n
    #url('^acceuil/?$', acceuil),
    #url('^index2/?$', index2),

    #url(r'^post/(?P<pk>\d+)$', PostDetail.as_view()),
                #retourner pk

]