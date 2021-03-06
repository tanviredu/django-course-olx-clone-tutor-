# Generated by Django 3.0.5 on 2020-05-10 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('logo', models.ImageField(upload_to='brand/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ad_type', models.CharField(choices=[('Sell', 'Sell'), ('Exchange', 'Exchange')], max_length=10)),
                ('condition', models.CharField(choices=[('New', 'New'), ('Excellent Condition', 'Excellent Condition'), ('Good Condition', 'Good Condition'), ('Bad Condition', 'Bad Condition')], max_length=20)),
                ('pay', models.CharField(choices=[('Cash', 'Cash'), ('Visa', 'Visa')], max_length=10)),
                ('image', models.ImageField(upload_to='product/')),
                ('description', models.TextField(max_length=1000)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='products.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='products.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
