from django.db import models
from django.contrib.auth.models import User
#from newsletter_subscription.models import SubscriptionBase

# Create your models here.

PEOPLE = (
    (0, "1"),
    (1, "2-4"),
    (2, "5-8"),
    (3, "więcej niż 8")
) 

AGE = (
    (0, "0-2"),
    (1, "3-5"),
    (2, "6-10"),
    (3, "11-13"),
    (4, "więcej niz 13")
)

DURATION = (
    (0, "do 30 min"),
    (1, "do 2 godzin"),
    (2, "kilka godzin"),
    (3, "cały dzień"),
    (4, "nieokreślony")
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

class AttrTag(models.Model):
    attr_tag = models.CharField(max_length=128)

    def __str__(self):
        return "{}" .format(self.attr_tag)


class AnimTag(models.Model):
    anim_tag = models.CharField(max_length=128)

    def __str__(self):
        return "{}" .format(self.anim_tag)

class GeneralFoto(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True, default="title")
    foto = models.FileField(upload_to="media/general")
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

class Wabik(models.Model):
    wabik_foto = models.ImageField(upload_to = "media/wabik/", blank=True, null=True)
    wabik_title = models.CharField(max_length=32, blank=True, null=True)
    wabik_info = models.CharField(max_length=150, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

class Attraction(models.Model):
    attr_name = models.CharField(max_length=128)
    address = models.CharField(max_length=64)
    attr_rating = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    description = models.TextField()
    rules = models.TextField()
    votes = models.IntegerField(blank=True, null=True)
    attr_tags = models.ManyToManyField(AttrTag)
    attr_foto = models.ManyToManyField(GeneralFoto)
    attr_people = models.IntegerField(choices=PEOPLE)
    attr_price = models.CharField(max_length=24)
    attr_duration = models.IntegerField(choices=DURATION)
    attr_www = models.CharField(max_length=128)
    attr_wabik = models.ManyToManyField(Wabik)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Atrakcja"
        verbose_name_plural = "Atrakcje"

    def __str__(self):
        return "{}" .format(self.attr_name)

class Animation(models.Model):
    anim_name = models.CharField(max_length=128)
    address = models.CharField(max_length=64)
    zakres = models.IntegerField(choices=ZAKRES)
    anim_rating = models.IntegerField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    description = models.TextField()
    rules = models.TextField()
    votes = models.IntegerField(blank=True, null=True)
    anim_tags = models.ManyToManyField(AnimTag)
    anim_foto = models.ManyToManyField(GeneralFoto)
    anim_people = models.IntegerField(choices=PEOPLE)
    anim_price = models.CharField(max_length=24)
    anim_duration = models.IntegerField(choices=DURATION)
    anim_www = models.CharField(max_length=128)
    anim_wabik = models.ManyToManyField(Wabik)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Animacja"
        verbose_name_plural = "Animacje"

    def __str__(self):
        return "{}" .format(self.anim_name)


class Newsletter(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "{}" .format(self.email)

class BlogTag(models.Model):
    blog_tag = models.CharField(max_length=128)

    def __str__(self):
        return "{}" .format(self.blog_tag)

class News(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    foto = models.FileField(upload_to="media/blog", blank=True, null=True)
    blog_tag = models.ManyToManyField(BlogTag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}" .format(self.title)

class Comment(models.Model):
    text = models.CharField(max_length=300)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}" .format(self.text)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    msg_content = models.TextField()
    sent = models.DateTimeField(auto_now_add = True)

    def __str__(self):
     return "{} {} {}".format(self.sender, self.receiver, self.msg_content)

