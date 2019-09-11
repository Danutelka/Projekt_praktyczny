from django import forms
from django.core.validators import URLValidator, EmailValidator
from django.core.exceptions import ValidationError
from .models import Attraction, Animation, TAGS_ATTR, PEOPLE, DURATION, TAGS_ANIM, ZAKRES

def validate_two_dots(value):
    if value.count('.') <2:
        raise ValidationError("za malo kropeczek")

class AddAtractionForm(forms.Form):
    attr_name = forms.CharField(label="Wpisz nazwę: ", max_length=128)
    address = forms.CharField(label="Wpisz adres: ", max_length=64)
    attr_rating = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    created = forms.DateField(widget=forms.HiddenInput)
    description = forms.CharField(widget=forms.Textarea(), label="opisz swoje usługi")
    rules = forms.CharField(widget=forms.Textarea(), label="opisz zasady i regulamin")
    votes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    attr_tag = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=TAGS_ATTR, label="Wybierz tagi")
    attr_foto1 = forms.ImageField(label="Dodaj foto 1:", help_text="możesz to zrobić później", required=False)
    attr_foto2 = forms.ImageField(label="Dodaj foto 2:", help_text="możesz to zrobić później", required=False)
    attr_foto3 = forms.ImageField(label="Dodaj foto 3:", help_text="możesz to zrobić później", required=False)
    attr_people = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=PEOPLE, label="wybierz liczbę osób")
    attr_price = forms.CharField(label="określ cenę", max_length=24)
    attr_duration = forms.ChoiceField(widget=forms.RadioSelect, label="czas trwania atrakcji", choices=DURATION)
    attr_www = forms.CharField(validators= [validate_two_dots, URLValidator()], label="podlinkuj swoja stronę www", max_length=32)
    attr1_foto = forms.ImageField(label="Special offer foto 1:", help_text="możesz to zrobić później", required=False)
    attr1_title = forms.CharField(label="Zatytułuj special offer 1", help_text="możesz to zrobić później", max_length=32, required=False)
    attr1_info = forms.CharField(widget=forms.Textarea(), label="Opisz special offer 1", help_text="możesz to zrobić później",max_length=150, required=False)
    attr2_foto = forms.ImageField(label="Special offer foto 2:", help_text="możesz to zrobić później", required=False)
    attr2_title = forms.CharField(label="Zatytułuj special offer 2", help_text="możesz to zrobić później", max_length=32, required=False)
    attr2_info = forms.CharField(widget=forms.Textarea(), label="Opisz special offer 2", help_text="możesz to zrobić później",max_length=150, required=False)
    attr3_foto = forms.ImageField(label="Special offer foto 3:", help_text="możesz to zrobić później", required=False)
    attr3_title = forms.CharField(label="Zatytułuj special offer 3", help_text="możesz to zrobić później", max_length=32, required=False)
    attr3_info = forms.CharField(widget=forms.Textarea(), label="Opisz special offer 3", help_text="możesz to zrobić później",max_length=150, required=False)

class AddAnimationForm(forms.Form):
    anim_name = forms.CharField(label="Wpisz nazwę: ", max_length=128)
    address = forms.CharField(label="Wpisz adres: ", max_length=64)
    zakres = forms.ChoiceField(widget=forms.RadioSelect, choices=ZAKRES, label="określ zasięg świadczonych usług")
    anim_rating = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    created = forms.DateField(widget=forms.HiddenInput)
    description = forms.CharField(widget=forms.Textarea(), label="opisz swoje usługi")
    rules = forms.CharField(widget=forms.Textarea(), label="opisz zasady i regulamin")
    votes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    anim_tag = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=TAGS_ANIM, label="Wybierz tagi")
    anim_foto1 = forms.ImageField(label="Dodaj foto 1:", help_text="możesz to zrobić później", required=False)
    anim_foto2 = forms.ImageField(label="Dodaj foto 2:", help_text="możesz to zrobić później", required=False)
    anim_foto3 = forms.ImageField(label="Dodaj foto 3:", help_text="możesz to zrobić później", required=False)
    anim_people = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=PEOPLE, label="wybierz liczbę osób")
    anim_price = forms.CharField(label="określ cenę", max_length=24)
    anim_duration = forms.ChoiceField(widget=forms.RadioSelect, label="czas trwania atrakcji", choices=DURATION)
    anim_www = forms.CharField(validators= [validate_two_dots, URLValidator()], label="podlinkuj swoja stronę www", max_length=32)
    anim1_foto = forms.ImageField(label="Special offer foto 1:", help_text="możesz to zrobić później", required=False)
    anim1_title = forms.CharField(label="Zatytułuj special offer 1", help_text="możesz to zrobić później", max_length=32, required=False)
    anim1_info = forms.CharField(widget=forms.Textarea(), label="Opisz special offer 1", help_text="możesz to zrobić później",max_length=150, required=False)
    anim2_foto = forms.ImageField(label="Special offer foto 2:", help_text="możesz to zrobić później", required=False)
    anim2_title = forms.CharField(label="Zatytułuj special offer 2", help_text="możesz to zrobić później", max_length=32, required=False)
    anim2_info = forms.CharField(widget=forms.Textarea(), label="Opisz special offer 2", help_text="możesz to zrobić później",max_length=150, required=False)
    anim3_foto = forms.ImageField(label="Special offer foto 3:", help_text="możesz to zrobić później", required=False)
    anim3_title = forms.CharField(label="Zatytułuj special offer 3", help_text="możesz to zrobić później", max_length=32, required=False)
    anim3_info = forms.CharField(widget=forms.Textarea(), label="Opisz special offer 3", help_text="możesz to zrobić później",max_length=150, required=False)




