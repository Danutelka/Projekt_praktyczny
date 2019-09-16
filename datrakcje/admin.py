from django.contrib import admin
from .models import Attraction, Animation, AttrTag, AnimTag, GeneralFoto, Wabik

# Register your models here.
admin.site.register(Attraction)
admin.site.register(Animation)
admin.site.register(AttrTag)
admin.site.register(AnimTag)
admin.site.register(GeneralFoto)
admin.site.register(Wabik)
