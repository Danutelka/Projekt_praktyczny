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
from datrakcje.views import StartView, AboutView, BaseView, BlogView, BlogSingleView,  \
    AtrakcjeView, AtrakcjeSingleView, AnimacjeView, AnimacjeSingleView, AddAtrakcjeView,  \
    AddAnimacjeView, AnimTagView, AttrTagView, AddAnimTagView, AddAttrTagView, AddGeneralFoto,  \
    LoginView, RegisterView, EditAtrakcje, EditAnimacje, ContactUsView, NewsletterView,  \
    NewsletterAnswerView, ResetPasswordView, NewsAddView, NewsEditView, SearchAttractionView,  \
    ComposeMessageView, ProfileView, SearchAnimationView, LogoutView
    #AttractionUpdate
    #ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', BaseView.as_view(), name="base"),
    path('index', StartView.as_view(), name="index"),
    path('about', AboutView.as_view(), name="about"),
    path('contact', ContactUsView.as_view(), name="contact"),
    path('newsletter', NewsletterView.as_view(), name="newsletter"),
    path('newsletter/answer', NewsletterAnswerView.as_view(), name="news-answer"),
    path('blog', BlogView.as_view(), name="blog"),
    path('blog/<int:pk>', BlogSingleView.as_view(), name="blog-single"),
    path('blog/add', NewsAddView.as_view(), name="blog-add"),
    path('blog/edit/<int:id>', NewsEditView.as_view(), name="blog-edit"),
    path('tagi/anim', AnimTagView.as_view(), name="tagi-animacje"),
    path('tagi/anim/add', AddAnimTagView.as_view(), name="new-anim-tag"),
    path('tagi/attr', AttrTagView.as_view(), name="tagi-atrakcje"),
    path('tagi/attr/add', AddAttrTagView.as_view(), name="new-attr-tag"),
    path('atrakcje', AtrakcjeView.as_view(), name="atrakcje"),
    path('atrakcje/<int:pk>', AtrakcjeSingleView.as_view(), name="atrakcje-single"),
    path('atrakcje/add', AddAtrakcjeView.as_view(), name="add-atrakcje"),
    path('atrakcje/edit/<int:pk>', EditAtrakcje.as_view(), name="edit-atrakcje"),
    #path('atrakcje/edit/<int:pk>', AttractionUpdate.as_view(), name="attr-update"),
    path('animacje', AnimacjeView.as_view(), name="animacje"),
    path('animacje/<int:pk>', AnimacjeSingleView.as_view(), name="animacje-single"),
    path('animacje/add', AddAnimacjeView.as_view(), name="add-animacje"),
    path('animacje/edit/<int:pk>', EditAnimacje.as_view(), name="edit-animacje"),
    path('foto/add', AddGeneralFoto.as_view(), name="dodaj-foto"),
    path('login', LoginView.as_view(), name="login"),
    path('logout/<int:pk>', LogoutView.as_view(), name="userlogout"),
    path('register', RegisterView.as_view(), name="register"),
    path('reset/password/<int:pk>', ResetPasswordView.as_view(), name="reset_password"),
    path('search1', SearchAttractionView.as_view(), name="search-atrakcje"),
    path('search2', SearchAnimationView.as_view(), name="search-animacje"),
    path('message/<int:pk>', ComposeMessageView.as_view(), name="add-message"),
    path('profile/<int:pk>', ProfileView.as_view(), name="profil")
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)




