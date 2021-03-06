# Generated by Django 2.2 on 2020-01-18 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scans', '0002_asset_ov_vulnerabilites_ov_vulnerabilities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset_Vulnerabilites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetid', models.IntegerField()),
                ('vulid', models.IntegerField()),
                ('scanid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerabilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetid', models.IntegerField()),
                ('cveid', models.TextField()),
                ('cwe', models.TextField()),
                ('cvss', models.IntegerField()),
                ('summary', models.TextField()),
                ('references', models.TextField()),
            ],
        ),
    ]
