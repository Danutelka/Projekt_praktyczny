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
from .models import Attraction, Animation, PEOPLE, AGE, DURATION, ZAKRES, AnimTag, AttrTag, GeneralFoto
from .forms import AddAtractionForm, AddAnimationForm, AddAttrTagForm, AddAnimTagForm,  \
    AddGeneralFotoForm, LoginForm, RegisterForm, SearchGeneralForm
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

class AttrTagView(View):
    def get(self, request):
        attrtag = AttrTag.objects.all()
        return TemplateResponse(request, 'attr-tags.html', context={"attrtag": attrtag})

class AddAttrTagView(View):
    def get(self, request):
        form = AddAttrTagForm()
        return TemplateResponse(request, 'add-attr-tag.html', context={'form': form})
    def post(self, request):
        form = AddAttrTagForm(request.POST)
        if form.is_valid():
            attr_tag = form.cleaned_data['attr_tag']
            AttrTag.objects.create(attr_tag=attr_tag)
            return HttpResponseRedirect('tagi/attr')

class AnimTagView(View):
    def get(self, request):
        animtag = AnimTag.objects.all()
        return TemplateResponse(request, 'anim-tags.html', context={"animtag": animtag})

class AddAnimTagView(View):
    def get(self, request):
        form = AddAnimTagForm()
        return TemplateResponse(request, 'add-anim-tags.html', context={"form": form})
    def post(self, request):
        form = AddAnimTagForm(request.POST)
        if form.is_valid():
            anim_tag = form.cleaned_data['anim_tag']
            AnimTag.objects.create(anim_tag=anim_tag)
            return HttpResponseRedirect('tagi/anim')

class AddGeneralFoto(View):
    def get(self, request):
        form = AddGeneralFotoForm()
        return TemplateResponse(request, 'add-general-foto.html', context={"form": form})
    def post(self, request):
        form = AddGeneralFotoForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            foto = form.cleaned_data['foto']
            GeneralFoto.objects.create(title=title, foto=foto)
            return HttpResponse("dodano pomyślnie")

class AtrakcjeView(View):
    def get(self, request):
        attr_all = Attraction.objects.all()
        return TemplateResponse(request, 'atrakcje.html', context={"attr_all": attr_all})

class AtrakcjeSingleView(View):
    #def get(self, request):
    #    return TemplateResponse(request, 'atrakcje-single.html')
    def get(self, request, pk):
        attr_single = get_object_or_404(Attraction, id=pk)
        # fotos = GeneralFoto.objecects.all()
        context ={
            "attr_single": attr_single,
            "people": PEOPLE,
            "age": AGE,
            "duration": DURATION,
            #"fotos": fotos
        }
        return TemplateResponse(request, 'atrakcje-single.html', context={"attr_single": attr_single,  \
                                "people": PEOPLE, "age": AGE, "duration": DURATION})

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
            attr_foto = form.cleaned_data['attr_foto']
            attr_people = form.cleaned_data['attr_people']
            attr_price = form.cleaned_data['attr_price']
            attr_duration = form.cleaned_data['attr_duration']
            attr_www = form.cleaned_data['attr_www']
            attr_wabik = form.cleaned_data['attr_wabik']
            Attraction.objects.create(attr_name=attr_name, address=address, description=description,  \
                rules=rules, attr_tag=attr_tag, attr_foto=attr_foto, attr_people=attr_people,  \
                attr_price=attr_price, attr_duration=attr_duration, attr_www=attr_www, attr_wabik=attr_wabik)
            return HttpResponseRedirect("atrakcje")

class AnimacjeView(View):
    def get(self, request):
        anim_all = Animation.objects.all()
        return TemplateResponse(request, 'animacje.html', context={"anim_all": anim_all})

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
    def post(self, request):
        form = AddAnimationForm(request.POST)
        if form.is_valid():
            anim_name = form.cleaned_data['anim_name']
            address = form.cleaned_data['address']
            zakres = form.cleaned_data['zakres']
            description = form.cleaned_data['description']
            rules = form.cleaned_data['rules']
            anim_tag = form.cleaned_data['anim_tag']
            anim_foto = form.cleaned_data['anim_foto']
            anim_people = form.cleaned_data['anim_people']
            anim_price = form.cleaned_data['anim_price']
            anim_duration = form.cleaned_data['anim_duration']
            anim_www = form.cleaned_data['anim_www']
            anim_wabik = form.cleaned_data['anim_wabik']
            Animation.objects.create(anim_name=anim_name, address=address, zakres=zakres,  \
                description=description, rules=rules, anim_tag=anim_tag, anim_foto=anim_foto,  \
                anim_people=anim_people, anim_price=anim_price, anim_duration=anim_duration,  \
                anim_www=anim_www, anim_wabik=anim_wabik)
            return HttpResponseRedirect("animacje")

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={'form':form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username, password = form.cleaned_data.values()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('zalogowany')
            else:
                return HttpResponse('ups niepoprawne logowanie')
        return render(request, 'login.html', context={'form':form})

def user_logout(request):
    logout(request)
    return redirect('/index')

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', context={'form':form})
    def post(self,request):
        form = RegisterForm(request.POST)
        error = []
        if form.is_valid():
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            if not User.objects.filter(username=username).exists():
                if password == password_again:
                    User.objects.create_user(username, password, first_name=first_name, last_name=last_name)
                    return HttpResponseRedirect("index")
                else:
                    error.append('Hasła są różne')
            else:
                error.append('użytkownik isnieje')
        return render(request, 'register.html', cotext={'form':form, 'error':error})

class SearchAttractionView(View):
    def get(self, request):
        form = SearchAttractionForm()
        return TemplateResponse(request, 'search-attr.html', context={'form': form})
    def post(self, request):
        form = SearchAttractionForm(request.POST)
        if form.is_valid():
            attr_name = form.cleaned_data['attr_name']
            attr_tag = form.cleaned_data['attr_tag']
            attr_people = form.cleaned_data['attr_people']
            address = form.cleaned_data['address']
            atrakcje1 = Attraction.objects.filter(attr_name__icontains=attr_name)
            atrakcje2 = Attraction.objects.filter(attr_tag__icontains=attr_tag)
            atrakcje3 = Attraction.objects.filter(attr_people__icontains=attr_people)
            atrakcje4 = Attraction.objects.filter(address__icontains=address)
            context = {
                "form": form,
                "atrakcje1": atrakcje1,
                "atrakcje2": atrakcje2,
                "atrakcje3": atrakcje3,
                "atrakcje4": atrakcje4
            }
        return TemplateResponse(request, "search-attr.html", context=context)

class SearchAttractionView(View):
    def get(self, request):
        form = SearchAnimationForm()
        return TemplateResponse(request, 'search-anim.html', context={'form': form})
    def post(self, request):
        form = SearchAnimationForm(request.POST)
        if form.is_valid():
            anim_name = form.cleaned_data['anim_name']
            anim_tags = form.cleaned_data['anim_tags']
            anim_people = form.cleaned_data['anim_people']
            zakres = form.cleaned_data['zakres']
            animacje1 = Animation.objects.filter(anim_name__icontains=anim_name)
            animacje2 = Animation.objects.filter(anim_tags__icontains=anim_tags)
            animacje3 = Animation.objects.filter(anim_people__icontains=anim_people)
            animacje4 = Animation.objects.filter(zakres__icontains=zakres)
            context = {
                "form": form,
                "animacje1": animacje1,
                "animacje2": animacje2,
                "animacje3": animacje3,
                "animacje4": animacje4
            }
        return TemplateResponse(request, "search-anim.html", context=context)

