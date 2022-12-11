# Generated by Django 4.1.2 on 2022-12-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_remove_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profileimages/'),
        ),
    ]
