# Generated by Django 4.2.1 on 2023-05-12 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_brand_flower'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
            ],
        ),
    ]
