# Generated by Django 3.2.16 on 2023-01-25 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20230125_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='table_no',
            field=models.CharField(max_length=2, null=True),
        ),
    ]