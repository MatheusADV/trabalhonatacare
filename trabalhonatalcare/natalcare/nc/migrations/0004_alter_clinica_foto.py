# Generated by Django 5.1.2 on 2024-11-16 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nc', '0003_alter_historico_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinica',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='trabalhonatalcare/natalcare/media'),
        ),
    ]
