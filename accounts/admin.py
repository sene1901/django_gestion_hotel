from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

# Désenregistrer si déjà enregistré (évite les erreurs)
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Configuration personnalisée de l'affichage User dans l'admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Colonnes affichées dans la liste
    list_display = ['username', 'email', 'is_active', 'is_staff', 'date_joined']
    
    # Filtres sur le côté
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'date_joined']
    
    # Barre de recherche
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    # Tri par défaut (du plus récent au plus ancien)
    ordering = ['-date_joined']
    
    # Organisation des champs dans le formulaire d'édition
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Champs en lecture seule
    readonly_fields = ['last_login', 'date_joined']