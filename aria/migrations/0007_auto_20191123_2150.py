# Generated by Django 2.2.7 on 2019-11-24 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aria', '0006_cropposition_croptype_growingstyle_plot_plotcoordinate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'genus',
            },
        ),
        migrations.RemoveField(
            model_name='crop',
            name='genus',
        ),
        migrations.RemoveField(
            model_name='crop',
            name='name',
        ),
        migrations.RemoveField(
            model_name='crop',
            name='species',
        ),
        migrations.AddField(
            model_name='crop',
            name='variety',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plot',
            name='garden',
            field=models.ForeignKey(db_column='garden', on_delete=django.db.models.deletion.CASCADE, to='aria.Plot'),
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=30)),
                ('genus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.Genus')),
            ],
        ),
        migrations.AddField(
            model_name='crop',
            name='taxonomy',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='aria.Species'),
            preserve_default=False,
        ),
    ]