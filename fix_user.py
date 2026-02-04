import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_django.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

print("=" * 50)
print("GESTION DES UTILISATEURS")
print("=" * 50)

# 1. Afficher tous les utilisateurs
print("\n📋 Liste de TOUS les utilisateurs :")
users = User.objects.all()
for user in users:
    print(f"  - Username: {user.username}")
    print(f"    Email: {user.email}")
    print(f"    Actif: {user.is_active}")
    print(f"    Staff: {user.is_staff}")
    print(f"    Superuser: {user.is_superuser}")
    print()

# 2. Activer l'utilisateur diawndieme@gmail.com
email_cible = 'diawndieme@gmail.com'
print(f"\n🔍 Recherche de {email_cible}...")

try:
    user = User.objects.get(email=email_cible)
    print(f"✅ Utilisateur trouvé !")
    print(f"   État actuel - Actif: {user.is_active}")
    
    if not user.is_active:
        user.is_active = True
        user.save()
        print(f"✅ Utilisateur {email_cible} ACTIVÉ avec succès !")
    else:
        print(f"ℹ️  L'utilisateur est déjà actif")
        
except User.DoesNotExist:
    print(f"❌ Utilisateur {email_cible} NON TROUVÉ")
    print(f"\n🆕 Création de l'utilisateur...")
    
    user = User.objects.create_user(
        username='ndieme',
        email=email_cible,
        password='sen@1901',
        is_active=True
    )
    print(f"✅ Utilisateur {email_cible} créé et activé !")

print("\n" + "=" * 50)
print("TERMINÉ")
print("=" * 50)