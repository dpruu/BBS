# Generated by Django 3.0.8 on 2020-08-06 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_bbs', '0011_auto_20200806_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='board_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='my_bbs.Board'),
        ),
    ]
