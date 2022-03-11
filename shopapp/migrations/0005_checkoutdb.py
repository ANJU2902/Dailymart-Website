# Generated by Django 3.2.6 on 2022-03-09 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_rename_cart_cartdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkoutdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('address', models.TextField(max_length=200, null=True)),
                ('cartid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopapp.cartdb')),
            ],
        ),
    ]