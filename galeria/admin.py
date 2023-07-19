from django.contrib import admin
from galeria.models import Fotografia, Categoria

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "categoria", "data_publicacao", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10

class ListandoCategorias(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 10
# Register your models here.
admin.site.register(Fotografia, ListandoFotografias)
admin.site.register(Categoria, ListandoCategorias)