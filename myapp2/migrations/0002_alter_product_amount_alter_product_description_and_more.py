# Generated by Django 4.2.6 on 2023-10-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]
