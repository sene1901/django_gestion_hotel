from django.db import migrations

def update_site(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    try:
        site = Site.objects.get(id=1)
        # En production, utiliser le domaine Vercel
        # En dev, cela n'affectera pas car on a déjà configuré localhost
        site.domain = 'django-hotel-eight.vercel.app'
        site.name = 'RED PRODUCT'
        site.save()
    except Site.DoesNotExist:
        Site.objects.create(
            id=1,
            domain='django-hotel-eight.vercel.app',
            name='RED PRODUCT'
        )

def reverse_update(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    try:
        site = Site.objects.get(id=1)
        site.domain = 'example.com'
        site.name = 'example.com'
        site.save()
    except Site.DoesNotExist:
        pass

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),  
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(update_site, reverse_update),
    ]
    
