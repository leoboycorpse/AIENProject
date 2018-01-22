from django.urls import path
from . import views
app_name = 'name'


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='aboutme'),
    path('contact',views.contact,name='contact'),
    path('test',views.test,name='Homepage'),
    path('contact/<str:name>',views.contact1),
    path('upload/',views.upload,name='upload'),
    path('test2',views.test2,name='test2'),

    path('Pagehome',views.Pagehome,name='Pagehome'),
    path('model',views.model,name='model'),
    path('price',views.price,name='price'),
    path('service',views.service,name='service'),
    path('area',views.area,name='area'),
    
    path('logins',views.logins,name='logins'),
    path('loginscheck',views.loginscheck,name='loginscheck'),
    path('logouts', views.logouts,name='logouts'),
    path('signup', views.signup,name='signup'),
    path('signupcheck',views.signupcheck,name='signupcheck'),
    path('checkorder',views.checkorder,name='checkorder'),
]

