# Generated by Django 3.2.20 on 2023-08-03 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]