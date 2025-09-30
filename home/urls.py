
from django.urls import path,include
from .views import *
urlpatterns = [

    path('',index),
    path('about_us',about_us),
    path('booking',booking),
    path('courses',courses),
    path('blog',blog),
    path('shop',shop),
    path('accounting',accounting),
    path('cttc',cttc),
    path('data_entry',data_entry),
    path('dca',dca),
    path('graphic',graphic),
    path('netfix',netfix),
    path('pddtp',pddtp),
    path('cctv',cctv),
    path('office',office),
    path('prog',prog),
    path('contact_us',contact_us),
]