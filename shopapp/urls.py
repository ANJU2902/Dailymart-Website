from django.urls import path
from django.urls.resolvers import URLPattern
from.import views 
urlpatterns=[
    path('',views.shop,name='shop'),
    path('contact',views.contact,name='contact'),
    path('getone',views.getone,name='getone'),
    path('message',views.message,name='message'),
    path('register',views.register,name='register'),
    path('regi',views.regi,name='regi'),
    path('registrations',views.registrations,name='registrations'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('userin',views.userin,name='userin'),
    path('logout',views.logout,name='logout'),
    path('vegetables',views.vegetables,name='vegetables'),
    path('fruits',views.fruits,name='fruits'),
    path('product/<str:cat>/',views.product,name='product'),
    path('single/<int:pid>/',views.single,name='single'),
    path('cart',views.cart,name='cart'),
    path('check',views.check,name='check'),
    path('cart1/<int:pid>/',views.cart1,name='cart1'),
    path('deletec/<int:cid>/',views.deletec,name='deletec'),
    path('checkout',views.checkout,name='checkout'),
    path('cart_update',views.cart_update,name='cart_update')
]

