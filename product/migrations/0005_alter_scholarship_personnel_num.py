# Generated by Django 4.1.5 on 2023-02-09 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='personnel_num',
            field=models.CharField(max_length=50),
        ),
    ]
