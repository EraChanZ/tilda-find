"""ProgTinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path
from polls.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/logout/', main),
    path('enter-page/',enter),
    path('register-page/',register),
    path('check/',check),
    path('auth/',auth),
    path('menu/',menu),
    path('search-page/',search),
    path('addteam/',team),
    path('algoritm-page/',algoritm),
    path('personal/',perspage),
    path('full/',full),
    path('admin-panel/',panel),
    path('change-info/',change)
]
#Add Django site authentication urls (for login, logout, password management)
#urlpatterns += [
    #url(r'^accounts/', include('django.contrib.auth.urls')),
#]
