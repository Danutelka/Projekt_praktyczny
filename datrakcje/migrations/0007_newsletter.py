# Generated by Django 2.0.12 on 2019-09-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datrakcje', '0006_auto_20190920_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
