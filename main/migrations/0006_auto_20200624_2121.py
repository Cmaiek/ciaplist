# Generated by Django 3.0.5 on 2020-06-24 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_shoppinglist_list_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='shopping_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ShoppingList'),
        ),
    ]
