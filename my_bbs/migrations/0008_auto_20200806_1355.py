# Generated by Django 3.0.8 on 2020-08-06 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_bbs', '0007_comment_bd_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='bd_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_bbs.Board'),
        ),
    ]