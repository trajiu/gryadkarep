from django.contrib import admin
from .models import *
# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    #list_display = ['id', 'name', 'email']
    list_display = [field.name for field in Subscriber._meta.fields]
    #fields = ['email'] #Отображать только поле email
    #exclude = ['email'] #Скрывать поле email
    #inlines = [] #
    list_filter = ['name', 'email']
    search_fields = ['name']
    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)