# Generated by Django 3.0 on 2020-09-21 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favoritos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritos', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]