# Generated by Django 4.2.5 on 2024-10-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whole_chickens', models.IntegerField(default=10)),
                ('legs', models.IntegerField(default=20)),
                ('wings', models.IntegerField(default=20)),
                ('flesh', models.IntegerField(default=10)),
            ],
        ),
    ]
