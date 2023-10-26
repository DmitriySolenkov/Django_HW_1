# Generated by Django 4.2.6 on 2023-10-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0002_alter_order_date_ordered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amount', models.IntegerField()),
                ('addition_date', models.DateTimeField()),
            ],
        ),
    ]