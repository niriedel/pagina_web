# Generated by Django 4.0.5 on 2022-06-09 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_autor_numobras_alter_obra_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='imagen',
            field=models.ImageField(null=True, upload_to='obrasimg'),
        ),
    ]
