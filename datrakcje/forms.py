from django import forms
from django.core.validators import URLValidator, EmailValidator
from django.core.exceptions import ValidationError
from .models import Attraction, Animation, PEOPLE, DURATION, ZAKRES, AttrTag, AnimTag,  \
    GeneralFoto, Wabik

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

class AddAtractionForm(forms.Form):
    attr_name = forms.CharField(label="Wpisz nazwę", max_length=128)
    address = forms.CharField(label="Wpisz adres", max_length=64)
    attr_rating = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    created = forms.DateField(widget=forms.HiddenInput)
    description = forms.CharField(widget=forms.Textarea(), label="Opisz swoje usługi")
    rules = forms.CharField(widget=forms.Textarea(), label="Opisz zasady i regulamin")
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

class SearchGeneralForm(forms.Form):
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