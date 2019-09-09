"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from datrakcje.views import StartView, AboutView, BaseView, ContactView, BlogView, BlogSingleView,  \
    AtrakcjeView, AtrakcjeSingleView, AnimacjeView, AnimacjeSingleView, AddAtrakcjeView,  \
    AddAnimacjeView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', BaseView.as_view(), name="base"),
    path('index', StartView.as_view(), name="index"),
    path('about', AboutView.as_view(), name="about"),
    path('contact', ContactView.as_view(), name="contact"),
    path('blog', BlogView.as_view(), name="blog"),
    path('blog/single', BlogSingleView.as_view(), name="blog-single"),
    path('atrakcje', AtrakcjeView.as_view(), name="atrakcje"),
    path('atrakcje/single', AtrakcjeSingleView.as_view(), name="atrakcje-single"),
    path('atrakcje/add', AddAtrakcjeView.as_view(), name="add-atrakcje"),
    path('animacje', AnimacjeView.as_view(), name="animacje"),
    path('animacje/single', AnimacjeSingleView.as_view(), name="animacje-single"),
    path('animacje/add', AddAnimacjeView.as_view(), name="add-animacje")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
