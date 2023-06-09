# Generated by Django 4.1.5 on 2023-02-09 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('personnel_num', models.IntegerField()),
                ('benefit', models.CharField(max_length=100)),
                ('target', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('view_num', models.IntegerField()),
            ],
        ),
    ]
