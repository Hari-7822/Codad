from django.contrib import admin
from django.urls import path, include
from .views.auth import *
from .views.common import *
from .views.Form import *
from .views.views import *


from django.conf.urls.static import static
from alpha import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import re_path
from django.views.static import serve


urlpatterns = []

admin_ = [
    path('admin/', admin.site.urls),    
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]

auth = [
    path('accounts/', include('django.contrib.auth.urls')),  # Use built-in authentication views
    path('enter_otp', enter_otp, name='enter_otp'),
    path('signup/<str:mail>', signup, name='signup'),
    path('login', user_login, name='login'),
]
common = [
    path('home/', home, name='homes'),
    path('home', home, name='home'),
    path('', co, name = "index"),
    path('serve_image_with_cors/', serve_image_with_cors, name='serve_image_with_cors'),
    path('serve_image_with_cors', serve_image_with_cors, name = "serve_image_with_cors"),
]
form = [
    path('apply', apply, name='apply'),
    path('applicant_list', applicant_list, name='applicant_list'),
]

urlpatterns.extend(auth)
urlpatterns.extend(common)
urlpatterns.extend(form)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()