# Generated by Django 2.0.5 on 2018-08-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_project', '0003_auto_20180803_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='Contact',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='Time_in',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='Time_out',
            field=models.TimeField(),
        ),
    ]
