# Generated by Django 3.1.7 on 2021-03-08 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210308_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='holder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.someuser'),
        ),
    ]
