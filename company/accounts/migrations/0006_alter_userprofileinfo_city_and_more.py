# Generated by Django 4.0.5 on 2022-06-04 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220603_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='city',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='contactno',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='portfolio_site',
            field=models.URLField(blank=True, null=True),
        ),
    ]
