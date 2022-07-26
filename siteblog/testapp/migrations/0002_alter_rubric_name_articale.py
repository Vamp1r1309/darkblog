# Generated by Django 4.0.6 on 2022-08-07 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Рубрики'),
        ),
        migrations.CreateModel(
            name='Articale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testapp.rubric')),
            ],
        ),
    ]
