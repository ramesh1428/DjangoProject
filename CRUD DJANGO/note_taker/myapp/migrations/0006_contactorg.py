# Generated by Django 4.1.3 on 2022-11-19 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactOrg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
