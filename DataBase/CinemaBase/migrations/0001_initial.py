# Generated by Django 3.2.3 on 2021-05-19 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CPL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subtitles', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
                ('disk_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KDM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('not_valid_before', models.DateTimeField(blank=True)),
                ('not_valid_after', models.DateTimeField(blank=True)),
                ('KDMKey', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Projector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('resolution', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SoundSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('technology', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SPL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('CPLs', models.ManyToManyField(blank=True, to='CinemaBase.CPL')),
                ('Effects', models.ManyToManyField(blank=True, to='CinemaBase.Effect')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(blank=True)),
                ('SPLs', models.ManyToManyField(to='CinemaBase.SPL')),
                ('cinema_hall', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CinemaBase.cinemahall')),
            ],
        ),
        migrations.AddField(
            model_name='cpl',
            name='KDM',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CinemaBase.kdm'),
        ),
        migrations.AddField(
            model_name='cinemahall',
            name='projector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CinemaBase.projector'),
        ),
        migrations.AddField(
            model_name='cinemahall',
            name='showings',
            field=models.ManyToManyField(blank=True, null=True, to='CinemaBase.Show'),
        ),
        migrations.AddField(
            model_name='cinemahall',
            name='sound_system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CinemaBase.soundsystem'),
        ),
    ]
