# Generated by Django 4.2 on 2023-06-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_variacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variável'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]
