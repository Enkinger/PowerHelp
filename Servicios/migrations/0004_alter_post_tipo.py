# Generated by Django 3.2.16 on 2022-12-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0003_alter_post_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tipo',
            field=models.CharField(choices=[['No Profesional', 'No Profesional'], ['Profesional', 'Profesional'], ['Empresa', 'Empresa'], ['ONG`S', 'ONG`S']], max_length=50),
        ),
    ]