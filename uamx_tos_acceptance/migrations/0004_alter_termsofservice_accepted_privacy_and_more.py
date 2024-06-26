# Generated by Django 4.2.8 on 2024-01-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uamx_tos_acceptance', '0003_rename_accepted_termsofservice_accepted_tos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termsofservice',
            name='accepted_privacy',
            field=models.BooleanField(default=False, verbose_name='He leído y acepto la política de privacidad de la UAM'),
        ),
        migrations.AlterField(
            model_name='termsofservice',
            name='accepted_tos',
            field=models.BooleanField(default=False, verbose_name='He leído y acepto los términos y condiciones de servicio'),
        ),
    ]
