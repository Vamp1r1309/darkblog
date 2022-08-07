# Generated by Django 4.0.6 on 2022-08-07 13:14

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_alter_rubric_name_articale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articale',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testapp.rubric'),
        ),
    ]
