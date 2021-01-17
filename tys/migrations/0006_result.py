# Generated by Django 3.0.5 on 2020-06-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tys', '0005_auto_20200624_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=3)),
                ('date', models.DateField()),
                ('stream', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'Result',
            },
        ),
    ]
