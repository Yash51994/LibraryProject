# Generated by Django 4.1.3 on 2023-01-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.IntegerField()),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]