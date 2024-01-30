# Generated by Django 4.2.8 on 2024-01-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uamx_tos_acceptance', '0002_alter_termsofservice_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='termsofservice',
            old_name='accepted',
            new_name='accepted_tos',
        ),
        migrations.AddField(
            model_name='termsofservice',
            name='accepted_privacy',
            field=models.BooleanField(default=False, verbose_name='Acepto la política de privacidad'),
        ),
    ]
