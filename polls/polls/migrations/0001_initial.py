# Generated by Django 2.1 on 2018-08-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(default='2', max_length=10)),
                ('tech', models.CharField(default='Technology', max_length=200)),
                ('teamname', models.CharField(default='teamname', max_length=200)),
                ('idea', models.CharField(default='idea', max_length=500)),
            ],
        ),
    ]