# Generated by Django 4.0.5 on 2022-07-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_cart_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=1),
        ),
    ]
