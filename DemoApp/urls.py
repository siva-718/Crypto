from django.urls import path
from . import views
urlpatterns=[
    #path('',views.home,name='home'),
    #path('about/',views.about,name='about'),
    #path('contact/',views.contact,name='contact'),
    #path('detail/',views.detail,name='detail'),
    #path('thanks/',views.thanks,name='thanks')"
    path('',views.index,name='index'),
    # path('calculation/',views.calculation,name='cal')
    ]