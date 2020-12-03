# Generated by Django 3.1.2 on 2020-12-03 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aria', '0008_plot_plt_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plot',
            name='plt_cr_num',
            field=models.ForeignKey(blank=True, db_column='plt_cr_num', null=True, on_delete=django.db.models.deletion.SET_NULL, to='aria.crop'),
        ),
        migrations.AlterField(
            model_name='plot',
            name='plt_parent_num',
            field=models.ForeignKey(blank=True, db_column='plt_parent_num', null=True, on_delete=django.db.models.deletion.CASCADE, to='aria.plot'),
        ),
    ]
