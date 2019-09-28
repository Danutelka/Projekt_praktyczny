from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.signing import BadSignature
from django.conf import settings
import django.contrib.auth.decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.conf.urls.static import static
from django.core.mail import send_mail
from .models import Attraction, Animation, PEOPLE, AGE, DURATION, ZAKRES, AnimTag, AttrTag, GeneralFoto,  \
    Wabik, Newsletter, BlogTag, News, Comment, Message
from .forms import AddAtractionForm, AddAnimationForm, AddAttrTagForm, AddAnimTagForm,  \
    AddGeneralFotoForm, LoginForm, RegisterForm, SearchGeneralForm, EditAtractionForm, EditAnimationForm,  \
    ContactUsForm, NewsletterForm, ResetPasswordForm, NewsAddForm, NewsEditForm, CommentAddForm,  \
    MessageForm
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

class BlogView(View):
    def get(self, request):
        news = News.objects.all().order_by('-posted_date')
        ctx = {
            "news" : news
        }
        return TemplateResponse(request, 'blog.html', ctx)

class BlogSingleView(View):
    #def get(self, request):
    #    return TemplateResponse(request, 'blog-single.html')
    def get(self, request, pk):
        news_single = get_object_or_404(News, id=pk)
        comments = Comment.objects.filter(news_id=news_single)
        #tags = BlogTag.objects.all()
        tagi = news_single.blog_tag.all()
        form = CommentAddForm()
        context ={
            "news_single": news_single,
            "comments": comments,
            #"tags": tags,
            "tagi": tagi,
            "form": form
        }
        return TemplateResponse(request, 'blog-single.html', context=context)
    def post(self, request, pk):
        news_single = get_object_or_404(News, id=pk)
        comments = Comment.objects.filter(news_id=news_single)
        tags = BlogTag.objects.all()
        form = CommentAddForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            data['user'] = str(request.user)
		    #data['news'] = request.session.get('news')
            Comment.objects.create(text=text)
            #comment = form.save(commit=False)
            #comment.news_single = news_single
            #comment.save()
            return HttpResponseRedirect('blog/<int:id>')
        return TemplateResponse(request, 'blog-single.html', context=context)

#@login_required
class NewsAddView(PermissionRequiredMixin, View):
    permission_required = "auth.add_news"
    def get(self, request):
        form = NewsAddForm()
        return TemplateResponse(request, 'blog-add.html', context={'form': form})
    def post(self, request):
        form = NewsAddForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            foto = form.cleaned_data['foto']
            blog_tag = form.cleaned_data['blog_tag']
            news = News.objects.create(title=title, content=content, foto=foto)
            news.blog_tag.set(blog_tag)
            news.save()
            return TemplateResponse(request, 'blog-answer.html')
        return TemplateResponse(request, 'blog-add.html', context={'form': form})

# class NewsEditView(PermissionRequiredMixin, UpdateView):
#     permission_required ="auth.change_news"
#     model = News
#     field = __all__
#     form = NewsEditForm

#@login_required
class NewsEditView(PermissionRequiredMixin, View):
    permission_required ="auth.change_news"
    def get(self, request, pk):
        form = NewsEditForm()
        new = News.objects.get(id=pk)
        ctx = {
            "form": form,
            "new": new
        }
        return TemplateResponse(request, 'blog-edit.html', ctx)
    def post(self, request, pk):
        form = NewsEditForm(request.POST, request.FILES)
        new = News.objects.get(id=pk)
        #p.first_name = request.POST.get('first_name')
        if form.is_valid():
            new.title = form.cleaned_data['title']
            new.content = form.cleaned_data['content']
            new.foto = form.cleaned_data['foto']
            new.blog_tag = form.cleaned_data['blog_tag']
            new.save()
            return HttpResponseRedirect("blog")

class AttrTagView(View):
    def get(self, request):
        attrtag = AttrTag.objects.all()
        return TemplateResponse(request, 'attr-tags.html', context={"attrtag": attrtag})

#@login_required
class AddAttrTagView(PermissionRequiredMixin, View):
    permission_required = "auth.add_attrtag"
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

#@login_required
class AddAnimTagView(PermissionRequiredMixin, View):
    permission_required = "auth.add_animtag"
    def get(self, request):
        form = AddAnimTagForm()
        return TemplateResponse(request, 'add-anim-tags.html', context={"form": form})
    def post(self, request):
        form = AddAnimTagForm(request.POST)
        if form.is_valid():
            anim_tag = form.cleaned_data['anim_tag']
            AnimTag.objects.create(anim_tag=anim_tag)
            return HttpResponseRedirect('tagi/anim')

#@login_required
class AddGeneralFoto(PermissionRequiredMixin, View):
    permission_required = "auth.add_generalfoto"
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
        attraction = Attraction.objects.all().order_by('-created')
        ctx = {
            "attraction" : attraction,
        }
        return TemplateResponse(request, 'atrakcje.html', ctx)

class AtrakcjeSingleView(View):
    def get(self, request, pk):
        attr_single = get_object_or_404(Attraction, id=pk)
        tagi = attr_single.attr_tags.all()
        #attraction_tags = Attraction.attr_tags.values_list('pk', flat=True)
       #tags = AttrTag.objects.all()
        fotos = GeneralFoto.objects.all()
        wabik = Wabik.objects.all()
        context ={
            "attr_single": attr_single,
            "people": PEOPLE,
            "age": AGE,
            "duration": DURATION,
        #    "tags" : tags,
            "fotos": fotos,
            "wabik": wabik,
            "tagi": tagi
        #    "attraction_tags": attraction_tags
        }
        return TemplateResponse(request, 'atrakcje-single.html', context=context)

#@login_required
class AddAtrakcjeView(PermissionRequiredMixin, View):
    permission_required = "auth.add_attraction"
    def get(self, request):
        form = AddAtractionForm()
        return TemplateResponse(request, 'add-atrakcje.html', context={'form':form})
    def post(self, request):
        form = AddAtractionForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print('form is valid')
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
            #user = form.cleaned_data['request.user.username']
            attraction = Attraction.objects.create(attr_name=attr_name, address=address, description=description,  \
                rules=rules, attr_people=attr_people, attr_price=attr_price,  \
                attr_duration=attr_duration, attr_www=attr_www, user=user)
            attraction.attr_tag.set(attr_tag)
            attraction.attr_foto.set(attr_foto)
            attraction.attr_wabik.set(attr_wabik)
            attraction.user = request.user.username
            attraction.save()
            return TemplateResponse(request, 'attr-answer.html')
        return TemplateResponse(request, 'add-atrakcje.html', context={'form':form})


#@login_required
class EditAtrakcje(PermissionRequiredMixin, View):
    permission_required = "auth.change_attraction"
    def get(self, request, pk):
        form = EditAtractionForm()
        atr = Attraction.objects.get(id=pk)
        ctx = {
            "form": form,
            "atr": atr
        }
        return TemplateResponse(request, 'edit-atrakcje.html', ctx)
    def post(self, request, pk):
        form = EditAtractionForm(request.POST, request.FILES)
        atr = Attraction.objects.get(id=pk)
        if form.is_valid():
            atr.attr_name = form.cleaned_data['attr_name']
            atr.address = form.cleaned_data['address']
            atr.description = form.cleaned_data['description']
            atr.rules = form.cleaned_data['rules']
            atr.attr_tag = form.cleaned_data['attr_tag']
            atr.attr_foto = form.cleaned_data['attr_foto']
            atr.attr_people = form.cleaned_data['attr_people']
            atr.attr_price = form.cleaned_data['attr_price']
            atr.attr_duration = form.cleaned_data['attr_duration']
            atr.attr_www = form.cleaned_data['attr_www']
            atr.attr_wabik = form.cleaned_data['attr_wabik']
            atr.save()
            return TemplateResponse(request, 'attr-answer.html')
        return TemplateResponse(request, 'edit-atrakcje.html', ctx)


class AnimacjeView(View):
    def get(self, request):
        animation = Animation.objects.all().order_by('-created')
        ctx = {
            "animation": animation
        }
        return TemplateResponse(request, 'animacje.html', ctx)

class AnimacjeSingleView(View):
    def get(self, request, pk):
        anim_single = get_object_or_404(Animation, id=pk)
        tagi = anim_single.anim_tags.all()
        #tags = AnimTag.objects.all()
        #fotos = GeneralFoto.objects.all()
        #wabik = Wabik.objects.all()
        context ={
            "anim_single": anim_single,
            "people": PEOPLE,
            "age": AGE,
            "duration": DURATION,
            "tagi": tagi
        #    "tags": tags,
        #    "fotos": fotos,
        #    "wabik": wabik
        }
        return TemplateResponse(request, 'animacje-single.html', context=context)

#@login_required
class AddAnimacjeView(PermissionRequiredMixin, View):
    permission_required = "auth.add_animation"
    def get(self, request):
        form = AddAnimationForm()
        return TemplateResponse(request, 'add-animacje.html', context={'form':form})
    def post(self, request):
        form = AddAnimationForm(request.POST, request.FILES)
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

#@login_required
class EditAnimacje(PermissionRequiredMixin, View):
    permission_required = "auth.change_animation"
    def get(self, request, pk):
        form = EditAnimationForm()
        anim = Animation.objects.get(id=pk)
        ctx = {
            "form": form,
            "anim": anim
        }
        return TemplateResponse(request, 'edit-animacje.html', ctx)
    def post(self, request, pk):
        form = EditAnimationForm(request.POST, request.FILES)
        anim = Animation.objects.get(id=pk)
        if form.is_valid():
            anim.anim_name = form.cleaned_data['anim_name']
            anim.address = form.cleaned_data['address']
            anim.zakres = form.cleaned_data['zakres']
            anim.description = form.cleaned_data['description']
            anim.rules = form.cleaned_data['rules']
            anim.anim_tag = form.cleaned_data['anim_tag']
            anim.anim_foto = form.cleaned_data['anim_foto']
            anim.anim_people = form.cleaned_data['anim_people']
            anim.anim_price = form.cleaned_data['anim_price']
            anim.anim_duration = form.cleaned_data['anim_duration']
            anim.anim_www = form.cleaned_data['anim_www']
            anim.anim_wabik = form.cleaned_data['anim_wabik']
            anim.save()
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
                #return HttpResponse('zalogowany')
                return TemplateResponse(request, 'zalogowano.html')
            else:
                return TemplateResponse(request, 'bad-login.html')
        return render(request, 'login.html', context={'form':form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return TemplateResponse(request, 'wylogowano.html')
    # def get(self, request, pk):
    #     user = get_object_or_404(User, id=pk)
    #     return TemplateResponse(request, 'logout.html', context={'user': user})
    # def post(self, request, pk):
    #     user = get_object_or_404(User, id=pk)
    #     if user is not None:
    #         logout(request)
    #         return HttpResponseRedirect('index')
    #     else:
    #         return TemplateResponse(request, 'logout.html', context={'user': user})
        

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
            log_on = form.cleaned_data['log_on']
            if not User.objects.filter(username=username).exists():
                if password == password_again:
                    User.objects.create_user(username, password, first_name=first_name, last_name=last_name, log_on=log_on)
                    return HttpResponseRedirect("index")
                else:
                    error.append('Hasła są różne')
            else:
                error.append('użytkownik isnieje')
        return render(request, 'register.html', context={'form':form, 'error':error})

#@login_required ????
class ResetPasswordView(View):
    def get(self, request, pk):
        form = ResetPasswordForm()
        # us=request.user()
        us = User.objects.get(id=pk)
        return TemplateResponse(request, 'reset_password.html', context={'form': form, 'us': us})
    def post(self, request, pk):
        form = ResetPasswordForm(request.POST)
        us = User.objects.get(id=pk)
        error=[]
        if form.is_valid():
            us.new_password = form.cleaned_data['new_password']
            us.new2_password = form.cleaned_data['new2_password']
            if us.new_password == us.new2_password:
                us.set_password(request.POST.get('new_password'))
                us.save()
            else:
                error.append('Hasła są różne - oba hasła muszą być jednakowe')
        return render(request, 'reset_password.html', context={'form':form, 'us': us, 'error':error})


class ContactUsView(View):
    def get(self, request):
        form = ContactUsForm()
        return TemplateResponse(request, 'contact.html', context={'form': form})
    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            temat = form.cleaned_data['temat']
            tekst = form.cleaned_data['tekst']
            # send email code goes here
            message = "{} wysłał/a wiadomość na temat {}, o treści {}".format(name, temat, tekst)
            send_mail('New Enquiry', message, email, ['contact@kiddme.com'])
            return TemplateResponse(request, 'contact-answer.html')
        else:
            return TemplateResponse(request, 'contact.html', context={'form': form})
        #return TemplateResponse(request, 'contact', {'form': form} 

class NewsletterView(View):
    def get(self, request):
        form = NewsletterForm()
        return TemplateResponse(request, 'newsletter.html', context={'form': form})
    def post(self, request):
        form = NewsletterForm(request.POST)
        error = []
        if form.is_valid():
            email = form.cleaned_data['email']
            is_active = form.cleaned_data['is_active']
            if not Newsletter.objects.filter(email=email).exists():
                Newsletter.objects.create(email=email, is_active=is_active)
                return TemplateResponse(request, 'news-answer.html')
            else:
                error.append('Na ten email pzesyłamy już nasz newsletter')
        return TemplateResponse(request, 'newsletter.html', context={'form':form, 'error':error})

class NewsletterAnswerView(View):
        def get(self, request):
            return TemplateResponse(request, 'news-answer.html')

# szukaczka

class SearchAttractionView(View):
    def get(self, request):
        form = SearchGeneralForm()
        return TemplateResponse(request, 'search_attr.html', context={'form': form})
    def post(self, request):
        form = SearchGeneralForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            atrakcje1 = Attraction.objects.filter(attr_name__icontains=name)
            #atrakcje2 = Attraction.objects.filter(attr_tag__icontains=name)
            context = {
                "form": form,
                "atrakcje1": atrakcje1,
                #"atrakcje2": atrakcje2
            }
        return TemplateResponse(request, "search_attr.html", context=context)

# class SearchAttractionView(View):
#     def get(self, request):
#         form = SearchAnimationForm()
#         return TemplateResponse(request, 'search-anim.html', context={'form': form})
#     def post(self, request):
#         form = SearchAnimationForm(request.POST)
#         if form.is_valid():
#             anim_name = form.cleaned_data['anim_name']
#             anim_tags = form.cleaned_data['anim_tags']
#             anim_people = form.cleaned_data['anim_people']
#             zakres = form.cleaned_data['zakres']
#             animacje1 = Animation.objects.filter(anim_name__icontains=anim_name)
#             animacje2 = Animation.objects.filter(anim_tags__icontains=anim_tags)
#             animacje3 = Animation.objects.filter(anim_people__icontains=anim_people)
#             animacje4 = Animation.objects.filter(zakres__icontains=zakres)
#             context = {
#                 "form": form,
#                 "animacje1": animacje1,
#                 "animacje2": animacje2,
#                 "animacje3": animacje3,
#                 "animacje4": animacje4
#             }
#         return TemplateResponse(request, "search-anim.html", context=context)

class SearchAnimationView(View):
    def get(self, request):
        form = SearchGeneralForm()
        return TemplateResponse(request, 'search_anim.html', context={'form': form})
    def post(self, request):
        form = SearchGeneralForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            animacje1 = Animation.objects.filter(anim_name__icontains=name)
            #atrakcje2 = Attraction.objects.filter(attr_tag__icontains=name)
            context = {
                "form": form,
                "animacje1": animacje1,
                #"atrakcje2": atrakcje2
            }
        return TemplateResponse(request, "search_anim.html", context=context)

class SearchBlogView(View):
    def get(self, request):
        form = SearchGeneralForm()
        return TemplateResponse(request, 'search_blog.html', context={'form': form})
    def post(self, request):
        form = SearchGeneralForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            blog1 = News.objects.filter(title__icontains=name)
            blog2 = News.objects.filter(content__icontains=name)
            context = {
                "form": form,
                "blog1": blog1,
                "blog2": blog2
            }
        return TemplateResponse(request, "search_blog.html", context=context)

#@login_required
class ComposeMessageView(PermissionRequiredMixin, View):
    permission_required = "auth.add_message"
    def get(self, request, pk):
        form = MessageForm()
        sender = User.objects.get(id=pk)
        return TemplateResponse(request, 'new-message.html', context={'form': form, 'sender': sender})
    def post(self, request, pk):
        form = MessageForm(request.POST)
        sender = User.objects.get(id=pk)
        if form.is_valid():
            receiver = form.cleaned_data['receiver']
            msg_content = form.cleaned_data['msg_content']
            Message.objects.create(receiver=receiver, msg_content=msg_content)
            return HttpResponseRedirect("profile/<int:pk>")

#@login_required
class MessageAllView(View):
    def get(self, request):
        messageall = Message.objects.all().order_by('-sent')
        return TemplateResponse(request, 'messages.html', context={'messageall': messageall})

#@login_required
class ProfileView(View):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        inbox = Message.objects.filter(receiver=user).order_by('-sent')
        sent = Message.objects.filter(sender=user).order_by('-sent')
        atrakcje = Attraction.objects.filter(user=user).order_by('-created')
        animacje = Animation.objects.filter(user=user).order_by('-created')
        context = {
            "user": user,
            "inbox": inbox,
            "sent": sent,
            "atrakcje": atrakcje,
            "animacje": animacje
            }
        return TemplateResponse(request, 'profile.html', context=context)
