# Generated by Django 3.2.3 on 2021-05-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userPanel', '0011_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Blue', 'Blue')], default='Active', max_length=150),
        ),
    ]
