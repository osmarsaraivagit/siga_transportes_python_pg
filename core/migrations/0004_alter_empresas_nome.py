# Generated by Django 4.2.7 on 2023-11-27 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_acertosviagens_options_alter_clientes_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]
