# Generated by Django 5.1.2 on 2024-11-16 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nc', '0007_alter_clinica_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinica',
            name='foto',
            field=models.ImageField(blank=True, default='/batman-resolve-in-the-rain.jpg', null=True, upload_to=''),
        ),
    ]