"""
URL configuration for kurooms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
	
from listings.forms import PropertyForm

from django.contrib.auth.forms import AuthenticationForm
from django import forms

class new(AuthenticationForm):
    username = forms.CharField(
        max_length=10,
        label = "Phone Number",
    )

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('listings/', include('listings.urls')),
    path('signup/', include('user.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=new)), 
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)