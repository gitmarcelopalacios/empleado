# Generated by Django 5.0 on 2023-12-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name', 'last_name']},
        ),
    ]
