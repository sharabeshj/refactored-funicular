# Generated by Django 2.0.4 on 2018-04-24 17:01

from django.db import migrations, models
import django.db.models.deletion
import hashid_field.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='0123456789abcdefghijklmnopqrstuvwxyz', min_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='0123456789abcdefghijklmnopqrstuvwxyz', min_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module', to='module.Project'),
        ),
    ]
