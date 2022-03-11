from django.urls import path
from django.urls.resolvers import URLPattern
from.import views
urlpatterns=[
    path('index',views.index,name='index'),
    path('category',views.category,name='category'),
    path('view',views.view,name='view'),
    path('getdata',views.getdata,name='getdata'),
    path('edit/<int:sid>/',views.edit,name='edit'),
    path('delete/<int:vid>/',views.delete,name='delete'),
    path('update/<int:wid>/',views.update,name='update'),
    path('addpro',views.addpro,name='addpro'),
    path('p_view',views.p_view,name='p_view'),
    path('getpro',views.getpro,name='getpro'),
    path('pedit/<int:mart1>/',views.pedit,name='pedit'),
    path('pdel/<int:mart2>/',views.pdel,name='pdel'),
    path('update1/<int:mart3>/',views.update1,name='update1'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adlogin',views.adlogin,name='adlogin'),
    path('order',views.order,name='order'),
    path('getorder',views.getorder,name='getorder')
]