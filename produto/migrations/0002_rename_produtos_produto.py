# Generated by Django 4.2 on 2023-06-04 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produtos',
            new_name='Produto',
        ),
    ]