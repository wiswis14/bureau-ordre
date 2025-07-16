from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('numero_texte', 'titre', 'secteur', 'date_enregistrement', 'type_document')
    search_fields = ('titre', 'numero_texte', 'secteur')
    list_filter = ('type_document', 'secteur', 'date_enregistrement')
