# Generated by Django 5.0 on 2023-12-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_empleado_hoja_vida_alter_empleado_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres Completos'),
        ),
    ]