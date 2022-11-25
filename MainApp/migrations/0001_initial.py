# Generated by Django 4.1.1 on 2022-11-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lang', models.CharField(max_length=30)),
                ('code', models.TextField(max_length=5000)),
                ('creation_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]