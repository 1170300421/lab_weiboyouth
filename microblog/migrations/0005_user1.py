# Generated by Django 3.0.7 on 2020-06-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0004_controlledhotspot1'),
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
