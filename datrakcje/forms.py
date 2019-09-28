from django import forms
from django.forms import ModelForm
from django.core.validators import URLValidator, EmailValidator
from django.core.exceptions import ValidationError
from .models import Attraction, Animation, PEOPLE, DURATION, ZAKRES, AttrTag, AnimTag,  \
    GeneralFoto, Wabik, Newsletter, News, Comment, BlogTag, User, Message

def validate_two_dots(value):
    if value.count('.') <2:
        raise ValidationError("za malo kropeczek")

class AddAttrTagForm(forms.Form):
    attr_tag = forms.CharField(max_length=128, label="Dodaj nowy tag dla atrakcji")

class AddAnimTagForm(forms.Form):
    anim_tag = forms.CharField(max_length=128, label="Dodaj nowy tag dla animacji")

class AddGeneralFotoForm(forms.Form):
    title = forms.CharField(label="Wpisz nazwę pliku: ", max_length=32)
    foto = forms.FileField()

class AddAtractionForm(forms.ModelForm):
        class Meta:
            model = Attraction
            exclude = ['user', 'attr_rating', 'created', 'votes' 'num_vote_up', 'num_vote_down', 'vote_score']

# class AddAtractionForm(forms.Form):
#     attr_name = forms.CharField(label="Wpisz nazwę", max_length=128)
#     address = forms.CharField(label="Wpisz adres", max_length=64)
#     attr_rating = forms.IntegerField(widget=forms.HiddenInput, initial=0)
#     created = forms.DateField(widget=forms.HiddenInput)
#     description = forms.CharField(widget=forms.Textarea(), label="Opisz swoje usługi")
#     rules = forms.CharField(widget=forms.Textarea(), label="Opisz zasady i regulamin")
#     votes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
#     attr_tags = forms.ModelMultipleChoiceField(queryset= AttrTag.objects.all(), widget=forms.CheckboxSelectMultiple, label="Wybierz tagi", help_text="* przytrzymaj klawisz Ctrl, aby dodać więcej niż 1")
#     attr_foto = forms.ModelMultipleChoiceField(queryset=GeneralFoto.objects.all(), widget=forms.CheckboxSelectMultiple, label="Dodaj foto", help_text="* możesz to zrobić później", required=False)
#     attr_people = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=PEOPLE, label="wybierz liczbę osób")
#     attr_price = forms.CharField(label="Określ cenę", max_length=24)
#     attr_duration = forms.ChoiceField(widget=forms.RadioSelect, label="Czas trwania atrakcji", choices=DURATION)
#     attr_www = forms.CharField(validators= [validate_two_dots, URLValidator()], label="Podlinkuj swoja stronę www", max_length=128)
#     attr_wabik = forms.ModelMultipleChoiceField(queryset=Wabik.objects.all(), widget=forms.CheckboxSelectMultiple, label="Special offer:", help_text="* możesz to zrobić później", required=False)
#     user = forms.CharField(widget=forms.HiddenInput)

class EditAtractionForm(forms.Form):
    attr_name = forms.CharField(label="Edytuj nazwę", max_length=128)
    address = forms.CharField(label="Edytuj adres", max_length=64)
    attr_rating = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    created = forms.DateField(widget=forms.HiddenInput)
    description = forms.CharField(widget=forms.Textarea(), label="Edytuj opis swoich usług")
    rules = forms.CharField(widget=forms.Textarea(), label="Edytuj opis zasad i regulaminu")
    votes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    attr_tag = forms.ModelMultipleChoiceField(queryset= AttrTag.objects.all(), widget=forms.CheckboxSelectMultiple, label="Wybierz tagi", help_text="* przytrzymaj klawisz Ctrl, aby dodać więcej niż 1")
    attr_foto = forms.ModelMultipleChoiceField(queryset=GeneralFoto.objects.all(), widget=forms.CheckboxSelectMultiple, label="Dodaj foto", help_text="* możesz to zrobić później", required=False)
    attr_people = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=PEOPLE, label="wybierz liczbę osób")
    attr_price = forms.CharField(label="Określ cenę", max_length=24)
    attr_duration = forms.ChoiceField(widget=forms.RadioSelect, label="Czas trwania atrakcji", choices=DURATION)
    attr_www = forms.CharField(validators= [validate_two_dots, URLValidator()], label="Podlinkuj swoja stronę www", max_length=128)
    attr_wabik = forms.ModelMultipleChoiceField(queryset=Wabik.objects.all(), widget=forms.CheckboxSelectMultiple, label="Special offer:", help_text="* możesz to zrobić później", required=False)

class AddAnimationForm(forms.Form):
    anim_name = forms.CharField(label="Wpisz nazwę", max_length=128)
    address = forms.CharField(label="Wpisz miasto", max_length=64)
    zakres = forms.ChoiceField(widget=forms.RadioSelect, choices=ZAKRES, label="Określ zasięg świadczonych usług")
    anim_rating = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    created = forms.DateField(widget=forms.HiddenInput)
    description = forms.CharField(widget=forms.Textarea(), label="Opisz swoje usługi")
    rules = forms.CharField(widget=forms.Textarea(), label="Opisz zasady i regulamin")
    votes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    anim_tag = forms.ModelMultipleChoiceField(queryset=AnimTag.objects.all(), widget=forms.CheckboxSelectMultiple, label="Wybierz tagi", help_text="* przytrzymaj klawisz Ctrl, aby dodać więcej niż 1")
    anim_foto = forms.ModelMultipleChoiceField(queryset=GeneralFoto.objects.all(), widget=forms.CheckboxSelectMultiple, label="Dodaj foto", help_text="* możesz to zrobić później", required=False)
    anim_people = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=PEOPLE, label="wybierz liczbę osób")
    anim_price = forms.CharField(label="Określ cenę", max_length=24)
    anim_duration = forms.ChoiceField(widget=forms.RadioSelect, label="Czas trwania atrakcji", choices=DURATION)
    anim_www = forms.CharField(validators= [validate_two_dots, URLValidator()], label="Podlinkuj swoja stronę www", max_length=128)
    anim_wabik = forms.ModelMultipleChoiceField(queryset=Wabik.objects.all(), widget=forms.CheckboxSelectMultiple, label="Special offer", help_text="* możesz to zrobić później", required=False)

class EditAnimationForm(forms.Form):
    anim_name = forms.CharField(label="Edytuj nazwę", max_length=128)
    address = forms.CharField(label="Edytuj miasto", max_length=64)
    zakres = forms.ChoiceField(widget=forms.RadioSelect, choices=ZAKRES, label="Zmień zasięg świadczonych usług")
    anim_rating = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    created = forms.DateField(widget=forms.HiddenInput)
    description = forms.CharField(widget=forms.Textarea(), label="Zmień opis swoje usługi")
    rules = forms.CharField(widget=forms.Textarea(), label="Zmień opis zasad i regulaminu")
    votes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    anim_tag = forms.ModelMultipleChoiceField(queryset=AnimTag.objects.all(), widget=forms.CheckboxSelectMultiple, label="Wybierz tagi", help_text="* przytrzymaj klawisz Ctrl, aby dodać więcej niż 1")
    anim_foto = forms.ModelMultipleChoiceField(queryset=GeneralFoto.objects.all(), widget=forms.CheckboxSelectMultiple, label="Dodaj foto", help_text="* możesz to zrobić później", required=False)
    anim_people = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=PEOPLE, label="wybierz liczbę osób")
    anim_price = forms.CharField(label="Określ cenę", max_length=24)
    anim_duration = forms.ChoiceField(widget=forms.RadioSelect, label="Czas trwania atrakcji", choices=DURATION)
    anim_www = forms.CharField(validators= [validate_two_dots, URLValidator()], label="Podlinkuj swoja stronę www", max_length=128)
    anim_wabik = forms.ModelMultipleChoiceField(queryset=Wabik.objects.all(), widget=forms.CheckboxSelectMultiple, label="Special offer", help_text="* możesz to zrobić później", required=False)


class LoginForm(forms.Form): 
    login = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput, max_length=10)

#def validate_username(value):
#    if value == "a":
#        raise ValidationError("Taki username istnieje")

class RegisterForm(forms.Form):
    username = forms.CharField(label="wpisz login", max_length=32)
    password = forms.CharField(widget=forms.PasswordInput(), label="wpisz hasło", max_length=10)
    password_again = forms.CharField(widget=forms.PasswordInput(), label="wpisz ponownie hasło", max_length=10)
    first_name = forms.CharField(label="wpisz imię", max_length=64)
    last_name = forms.CharField(label="wpisz nazwisko", max_length=64)
    email = forms.CharField(validators=[EmailValidator()])
    log_on = forms.BooleanField(label="Logowanie po rejestracji:",required=False)

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(), label="wprowadź nowe hasło")
    new2_password = forms.CharField(widget=forms.PasswordInput(), label="wpisz ponownie nowe hasło")

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, label="Wpisz Twoje imię")
    email = forms.EmailField(label="Wpisz email")
    temat = forms.CharField(max_length=100, label="Określ temat")
    tekst = forms.CharField(widget=forms.Textarea(), label="Wpisz treść wiadomości")

class NewsletterForm(forms.Form):
    email = forms.EmailField(label="Wpisz email", max_length=150)
    is_active = forms.BooleanField(initial=False, label="Zgadzam się na przesyłanie newslettera")

class NewsAddForm(forms.ModelForm):
        class Meta:
            model = News
            exclude = ['user', 'posted_date', 'num_vote_up', 'num_vote_down', 'vote_score']

    # title = forms.CharField(max_length=250, label="wpisz tytuł posta")
    # content = forms.TextField(widget=forms.Textarea(), label="wpisz treść posta")
    # foto = forms.FileField(blank=True, null=True)
    # blog_tag = forms.ModelMultipleChoiceField(queryset=BlogTag.objects.all(), widget=forms.CheckboxSelectMultiple, label="wybierz tagi postu")
    # user = forms.ModelChoiceField(queryset=User.objects.filter(user=username), widget=forms.HiddenInput)
    # posted_date = forms.DateField(widget=forms.HiddenInput)

class NewsEditForm(forms.Form):
    title = forms.CharField(max_length=250, label="edytuj tytuł posta")
    content = forms.CharField(widget=forms.Textarea(), label="edytuj treść posta")
    foto = forms.FileField(required=False)
    blog_tag = forms.ModelMultipleChoiceField(queryset=BlogTag.objects.all(), widget=forms.CheckboxSelectMultiple, label="edytuj tagi postu")
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)
    posted_date = forms.DateField(widget=forms.HiddenInput)

# class CommentAddForm(forms.Form):
#     text = forms.CharField(max_length=300, label="zostaw komentarz")
#     news = forms.ModelMultipleChoiceField(queryset=News.objects.all(), on_delete=models.CASCADE, widget=forms.HiddenInput)
#     user = forms.ModelMultipleChoiceField(queryset=User.object.filter(user=username), on_delete=models.CASCADE, widget=forms.HiddenInput)
#     posted_date = models.DateTimeField(auto_now_add=True, widget=forms.HiddenInput)

class CommentAddForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(), max_length=300, label="Treść komentarza")
    class Meta:
        model = Comment
        exclude = ['news', 'user', 'posted_date']

class SearchGeneralForm(forms.Form):
    name = forms.CharField(label="wyszukaj")

class SearchForm(forms.Form):
    name = forms.CharField(label="wyszukaj")

class SearchAtractionForm(forms.Form):
    attr_name = forms.CharField(max_length=20, label="znajdź po nazwie", required=False)
    attr_tag = forms.ModelMultipleChoiceField(queryset= AttrTag.objects.all(), label="znajdź po tagu", required=False)
    attr_people = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=PEOPLE, label="szukaj policzbę osób", required=False)
    address = forms.CharField(label="Miejscowość:", max_length=24, required=False)

class SearchAnimationForm(forms.Form):
    anim_name = forms.CharField(max_length=20, label="znajdź po nazwie", required=False)
    anim_tags = forms.ModelMultipleChoiceField(queryset= AnimTag.objects.all(), label="znajdź po tagu", required=False)
    anim_people = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=PEOPLE, label="szukaj policzbę osób", required=False)
    zakres = forms.ChoiceField(widget=forms.RadioSelect, choices=ZAKRES, label="zasięg usług", required=False)

class MessageForm(forms.Form):
    msg_content = forms.CharField(widget=forms.Textarea(), label="Treść wiadomości")
    class Meta:
        model = Message
        exclude = ['sender', 'sent']