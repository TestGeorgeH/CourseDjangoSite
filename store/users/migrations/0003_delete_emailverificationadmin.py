# Generated by Django 4.1.7 on 2023-04-02 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emailverification_user_is_verified_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailVerificationAdmin',
        ),
    ]