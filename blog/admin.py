from django.contrib import admin
from .models import Post

# Register your models here.


class postadminshow(admin.ModelAdmin):
    display_list=['title','author','time_publish','time_created']
    

admin.site.register(Post,postadminshow)
