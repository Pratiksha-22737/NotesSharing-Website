from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.login1, name='login'),
    path('signup', views.signup, name='signup'),
    path('signupinfohandle', views.signupinfohandle, name='signupinfohandle'),
    path('loginhandle', views.loginhandle, name='loginhandle'),
    path('logouthandle', views.logouthandle, name='logouthandle'),
    path('csfy', views.csfy, name='csfy'),
    path('cssy', views.cssy, name='cssy'),
    path('csty', views.csty, name='csty')
]
urlpatterns  = urlpatterns +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)