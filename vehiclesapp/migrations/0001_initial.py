# Generated by Django 3.2.20 on 2023-08-04 03:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=15)),
                ('speed', models.IntegerField()),
                ('acceraltion', models.IntegerField()),
                ('durability', models.IntegerField()),
                ('handling', models.IntegerField()),
                ('traction', models.IntegerField()),
            ],
        ),
    ]