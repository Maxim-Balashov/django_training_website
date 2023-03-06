# Generated by Django 4.1.7 on 2023-03-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_phone',
            field=models.CharField(max_length=200, verbose_name='Телефон'),
        ),
    ]