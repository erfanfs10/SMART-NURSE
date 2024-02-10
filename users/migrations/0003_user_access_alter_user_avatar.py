# Generated by Django 4.2 on 2024-02-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='access',
            field=models.CharField(blank=True, choices=[('C', 'CENTER_OWNER'), ('N', 'NURSE'), ('P', 'PATIENT')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='default_avatar.png', null=True, upload_to='avatars'),
        ),
    ]
