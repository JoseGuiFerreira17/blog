# Generated by Django 2.0.13 on 2020-01-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data_publicacao',
            field=models.DateTimeField(),
        ),
    ]