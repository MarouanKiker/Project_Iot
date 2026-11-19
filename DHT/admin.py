from django.contrib import admin
from .models import Dht11, Operateur, Incident


@admin.register(Dht11)
class Dht11Admin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'humidity', 'date')
    list_filter = ('date',)
    ordering = ('-date',)
    search_fields = ('id',)


@admin.register(Operateur)
class OperateurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'adresse', 'tel')
    search_fields = ('nom', 'adresse', 'tel')
    ordering = ('nom',)


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'temperature', 'status', 'operateur', 'description')
    list_filter = ('status', 'date')
    search_fields = ('description', 'operateur__nom')
    ordering = ('-date',)
    autocomplete_fields = ('operateur',)
