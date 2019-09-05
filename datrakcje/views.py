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