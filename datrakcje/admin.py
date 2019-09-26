from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin
from .models import Attraction, Animation, AttrTag, AnimTag, GeneralFoto, Wabik, Newsletter,  \
    BlogTag, News, Comment, Message

# Register your models here.
@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    exclude = ['attr_rating', 'created', 'votes'] 

@admin.register(Animation)
class AnimationAdmin(admin.ModelAdmin):
    exclude = ['anim_rating', 'created', 'votes']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    exclude = ['posted_date']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    exclude =['news', 'user', 'posted_date']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    exclude = ['sent']

admin.site.register(AttrTag)
admin.site.register(AnimTag)
admin.site.register(BlogTag)
admin.site.register(GeneralFoto)
admin.site.register(Wabik)
admin.site.register(Newsletter)

