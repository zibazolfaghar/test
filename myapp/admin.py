from django.contrib import admin

# Register your models here.
from .models import book


class AdminMode(admin.ModelAdmin):
  list_display = ['__str__','Author','store_name','fav']
  search_fields = ['Author','store_name']

admin.site.register(book,AdminMode)
