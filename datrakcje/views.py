from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
import django.contrib.auth.decorators
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.conf.urls.static import static
from .models import Attraction, Animation, PEOPLE, AGE, DURATION, TAGS_ANIM, TAGS_ATTR, ZAKRES
from .forms import AddAtractionForm, AddAnimationForm
# Create your views here.

class BaseView(View):
    def get(self, request):
        return TemplateResponse(request, 'base.html')

class StartView(View):
    def get(self, request):
        return TemplateResponse(request, 'index.html')

class AboutView(View):
    def get(self, request):
        return TemplateResponse(request, 'about.html')

class ContactView(View):
    def get(self, request):
        return TemplateResponse(request, 'contact.html')

class BlogView(View):
    def get(self, request):
        return TemplateResponse(request, 'blog.html')

class BlogSingleView(View):
    def get(self, request):
        return TemplateResponse(request, 'blog-single.html')

class AtrakcjeView(View):
    def get(self, request):
        return TemplateResponse(request, 'atrakcje.html')

class AtrakcjeSingleView(View):
    def get(self, request):
        return TemplateResponse(request, 'atrakcje-single.html')

class AddAtrakcjeView(View):
    def get(self, request):
        form = AddAtractionForm()
        return TemplateResponse(request, 'add-atrakcje.html', context={'form':form})

class AnimacjeView(View):
    def get(self, request):
        return TemplateResponse(request, 'animacje.html')

class AnimacjeSingleView(View):
    def get(self, request):
        return TemplateResponse(request, 'animacje-single.html')

class AddAnimacjeView(View):
    def get(self, request):
        form = AddAnimationForm()
        return TemplateResponse(request, 'add-animacje.html', context={'form':form})
