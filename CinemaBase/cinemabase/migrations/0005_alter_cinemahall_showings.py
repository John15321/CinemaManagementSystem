# Generated by Django 3.2.2 on 2021-05-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemabase', '0004_alter_cinemahall_showings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemahall',
            name='showings',
            field=models.ManyToManyField(blank=True, to='cinemabase.Show'),
        ),
    ]
