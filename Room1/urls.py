from . import views
from django.urls import include,path



urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('nav',views.nav, name='nav'),
    path('signin',views.signin, name='signin'),
    path('signup',views.signup, name='signup'),
    
    
     path('__reload__/', include('django_browser_reload.urls')),#removed after production
    
]