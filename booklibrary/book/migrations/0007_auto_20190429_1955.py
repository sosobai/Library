# Generated by Django 2.2 on 2019-04-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_suser_headpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suser',
            name='headpic',
            field=models.ImageField(blank=True, null=True, upload_to='userpic'),
        ),
    ]
