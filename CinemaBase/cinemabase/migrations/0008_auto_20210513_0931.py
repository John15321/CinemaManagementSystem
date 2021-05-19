# Generated by Django 3.2.2 on 2021-05-13 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemabase', '0007_auto_20210513_0905'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Show',
            new_name='ShowEntity',
        ),
        migrations.AlterField(
            model_name='cinemahall',
            name='showings',
            field=models.ManyToManyField(to='cinemabase.Show'),
        ),
        migrations.AlterField(
            model_name='showentity',
            name='cinema_hall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinemabase.cinemahall'),
        ),
    ]