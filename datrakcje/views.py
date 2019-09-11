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
        #attr_all = Attraction.objects.all().
        return TemplateResponse(request, 'atrakcje.html') #, context={"attr_all": attr_all})

class AtrakcjeSingleView(View):
    def get(self, request):
        return TemplateResponse(request, 'atrakcje-single.html')
    #def get(self, request, pk):
        #attr_single = get_object_or_404(Attraction, id=pk)
        #context ={
        #    "attr_single": attr_single
        #}
        #return TemplateResponse(request, 'atrakcje-single.html', context)


#class AddAtractionView(CreateView):
#    model = Attraction
#    fields = '__all__'
#    success_url = ("atrakcje")

class AddAtrakcjeView(View):
    def get(self, request):
        form = AddAtractionForm()
        return TemplateResponse(request, 'add-atrakcje.html', context={'form':form})
    def post(self, request):
        form = AddAtractionForm(request.POST)
        if form.is_valid():
            attr_name = form.cleaned_data['attr_name']
            address = form.cleaned_data['address']
            description = form.cleaned_data['description']
            rules = form.cleaned_data['rules']
            attr_tag = form.cleaned_data['attr_tag']
            attr_foto1 = form.cleaned_data['attr_foto1']
            attr_foto2 = form.cleaned_data['attr_foto2']
            attr_foto3 = form.cleaned_data['attr_foto3']
            attr_people = form.cleaned_data['attr_people']
            attr_price = form.cleaned_data['attr_price']
            attr_duration = form.cleaned_data['attr_duration']
            attr_www = form.cleaned_data['attr_www']
            attr1_foto = form.cleaned_data['attr1_foto']
            attr1_title = form.cleaned_data['attr1_title']
            attr1_info = form.cleaned_data['attr1_info']
            attr2_foto = form.cleaned_data['attr2_foto']
            attr2_title = form.cleaned_data['attr2_title']
            attr2_info = form.cleaned_data['attr2_info']
            attr3_foto = form.cleaned_data['attr3_foto']
            attr3_title = form.cleaned_data['attr3_title']
            attr3_info = form.cleaned_data['attr3_info']
            Attraction.objects.create(attr_name=attr_name, address=address, description=description,  \
                rules=rules, attr_tag= attr_tag, attr_foto1= attr_foto1, attr_foto2=attr_foto2,  \
                attr_people=attr_people, attr_price=attr_price, attr_duration=attr_duration,  \
                attr_www=attr_www, attr1_foto=attr1_foto, attr1_title=attr1_title,  \
                attr1_info=attr1_info, attr2_foto=attr2_foto, attr2_title=attr2_title,  \
                attr2_info=attr2_info, attr3_foto=attr3_foto, attr3_title=attr3_title,  \
                attr3_info=attr3_info)
            return HttpResponseRedirect("atrakcje")


class AnimacjeView(View):
    def get(self, request):
        #anim_all = Animation.objects.all().
        return TemplateResponse(request, 'animacje.html') #, context={"anim_all": anim_all})

class AnimacjeSingleView(View):
    def get(self, request):
        return TemplateResponse(request, 'animacje-single.html')
    #def get(self, request, pk):
        #anim_single = get_object_or_404(Animation, id=pk)
        #context ={
        #    "anim_single": anim_single
        #}
        #return TemplateResponse(request, 'animacje-single.html', context)


class AddAnimacjeView(View):
    def get(self, request):
        form = AddAnimationForm()
        return TemplateResponse(request, 'add-animacje.html', context={'form':form})
