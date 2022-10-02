# Generated by Django 4.1.1 on 2022-10-02 05:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sitioweb', '0005_categoria_created_categoria_updated_producto_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='producto',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]