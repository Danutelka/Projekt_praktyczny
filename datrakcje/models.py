from django.db import models

# Create your models here.

PEOPLE = (
    (0, "1"),
    (1, "2-4"),
    (2, "5-8"),
    (3, "więcej")
) 

AGE = (
    (0, "0-2"),
    (1, "3-5"),
    (2, "6-10"),
    (3, "11-13"),
    (4, "więcej")
)

DURATION = (
    (0, "do 30 min"),
    (1, "do 2 godzin"),
    (2, "kilka godzin"),
    (3, "cały dzień"),
    (4, "nieokreślony")
)

TAGS_ATTR = (
    (0, "Wystawa"),
    (1, "Centrum Nauki"),
    (2, "Park"),
    (3, "Park Rozrywki"),
    (4, "Park Linowy"),
    (5, "Park Miniatur"),
    (6, "Ogród"), 
    (7, "Centrum Zabaw"),
    (8, "Zoo"),
    (9, "Plac zabaw"),
    (10, "Wodny Plac zabaw"),
    (11, "AguaPark"),
    (12, "Tor sanezckowy"),
    (13, "Farma"),
    (14, "Sport"),
    (15, "Event"),
    (16, "Nietypowe"),
    (17, "Przyjazne niepełnosprawnym"),
    (18, "Dostępne po angielsku")
)

TAGS_ANIM = (
    (0, "Wata cukrowa"),
    (1, "Balony z helem"),
    (2, "Żywe maskotki"),
    (3, "Tematyczne"),
    (4, "Teatr"),
    (5, "Wypożyczalnia"),
    (6, "Balonowe Zoo"),
    (7, "Konkursy"),
    (8, "Kreatywne zabawy"),
    (9, "Świat baniek"),
    (10, "Zabawy ruchowe"),
    (11, "Sport"),
    (12, "Zagadki"),
    (13, "Gry"),
    (14, "Piniata"),
    (15, "Nietypowe"),
    (16, "Przyjazne niepełnosprawnym"),
    (17, "Dostępne po angielsku")
)

ZAKRES =(
    (0, "moja miejsowość"),
    (1, "dolnośląskie"),
    (2, "kujawsko-pomorskie"),
    (3, "lubelskie"),
    (4, "lubuskie"),
    (5, "łódzkie"),
    (6, "małopolskie"),
    (7, "mazowieckie"),
    (8, "opolskie"),
    (9, "podkarpackie"),
    (10, "podlaskie"),
    (11, "pomorskie"),
    (12, "śląskie"),
    (13, "świętokrzyskie"),
    (14, "warmińsko-mazurskie"),
    (15, "wielkopolskie"),
    (16, "zachodniopomorskie"),
    (17, "cały kraj")
)
class Attraction(models.Model):
    attr_name = models.CharField(max_length=128)
    address = models.CharField(max_length=64)
    attr_rating = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    description = models.TextField()
    rules = models.TextField()
    votes = models.IntegerField(blank=True, null=True)
    attr_tag = models.IntegerField(choices=TAGS_ATTR)
    attr_foto1 = models.ImageField(upload_to = "media/attr/", blank=True, null=True)
    attr_foto2 = models.ImageField(upload_to = "media/attr/", blank=True, null=True)
    attr_foto3 = models.ImageField(upload_to = "media/attr/", blank=True, null=True)
    attr_people = models.IntegerField(choices=PEOPLE)
    attr_price = models.CharField(max_length=24)
    attr_duration = models.IntegerField(choices=DURATION)
    attr_www = models.CharField(max_length=32)
    attr1_foto = models.ImageField(upload_to="media/attr/", blank=True, null=True)
    attr1_title = models.CharField(max_length=32, blank=True, null=True)
    attr1_info = models.CharField(max_length=150, blank=True, null=True)
    attr2_foto = models.ImageField(upload_to="media/attr/", blank=True, null=True)
    attr2_title = models.CharField(max_length=32, blank=True, null=True)
    attr2_info = models.CharField(max_length=150, blank=True, null=True)
    attr3_foto = models.ImageField(upload_to="media/attr/", blank=True, null=True)
    attr3_title = models.CharField(max_length=32, blank=True, null=True)
    attr3_info = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Atrakcja"
        verbose_name_plural = "Atrakcje"

    def __str__(self):
        return "{}" .format(self.attr_name)

class Animation(models.Model):
    anim_name = models.CharField(max_length=128)
    address = models.CharField(max_length=64)
    zakres = models.IntegerField(choices=ZAKRES)
    anim_rating = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    description = models.TextField()
    rules = models.TextField()
    votes = models.IntegerField(blank=True, null=True)
    anim_tag = models.IntegerField(choices=TAGS_ANIM)
    anim_foto1 = models.ImageField(upload_to = "media/anim/", blank=True, null=True)
    anim_foto2 = models.ImageField(upload_to = "media/anim/", blank=True, null=True)
    anim_foto3 = models.ImageField(upload_to = "media/anim/", blank=True, null=True)
    anim_people = models.IntegerField(choices=PEOPLE)
    anim_price = models.CharField(max_length=24)
    anim_duration = models.IntegerField(choices=DURATION)
    anim_www = models.CharField(max_length=32)
    anim1_foto = models.ImageField(upload_to="media/anim/", blank=True, null=True)
    anim1_title = models.CharField(max_length=32, blank=True, null=True)
    anim1_info = models.CharField(max_length=150, blank=True, null=True)
    anim2_foto = models.ImageField(upload_to="media/anim/", blank=True, null=True)
    anim2_title = models.CharField(max_length=32, blank=True, null=True)
    anim2_info = models.CharField(max_length=150, blank=True, null=True)
    anim3_foto = models.ImageField(upload_to="media/anim/", blank=True, null=True)
    anim3_title = models.CharField(max_length=32, blank=True, null=True)
    anim1_info = models.CharField(max_length=150, blank=True, null=True)


    class Meta:
        verbose_name = "Animacja"
        verbose_name_plural = "Animacje"

    def __str__(self):
        return "{}" .format(self.anim_name)