# Generated by Django 4.0.5 on 2022-06-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatRecords',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('birth_date', models.DateTimeField(db_column='birthDate')),
            ],
        ),
    ]
