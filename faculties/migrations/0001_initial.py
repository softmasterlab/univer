# Generated by Django 3.0.2 on 2020-01-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('about', models.TextField(max_length=300)),
                ('content', models.TextField(max_length=1024)),
                ('picture', models.FileField(upload_to='pictures/')),
                ('photo', models.FileField(upload_to='photo/')),
                ('site', models.URLField()),
            ],
        ),
    ]
