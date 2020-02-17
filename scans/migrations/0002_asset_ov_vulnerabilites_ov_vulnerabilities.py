# Generated by Django 2.2 on 2020-01-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset_OV_Vulnerabilites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetid', models.IntegerField()),
                ('ovid', models.IntegerField()),
                ('scanid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OV_Vulnerabilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cveid', models.TextField()),
                ('vulnname', models.TextField()),
                ('severity', models.TextField()),
                ('location', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
