from django.contrib import admin
from .models import Fotografia

class ListandoFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicado")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria","usuario",)
    list_editable = ("publicado",)
    list_per_page = 5
    
    
admin.site.register(Fotografia, ListandoFotografia)

