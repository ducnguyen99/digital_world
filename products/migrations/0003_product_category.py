# Generated by Django 3.1 on 2020-08-23 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200823_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PS4', 'PS4'), ('Nitendo Switch', 'Nitendo Switch'), ('PC Gaming', 'PC Gaming')], max_length=120, null=True),
        ),
    ]