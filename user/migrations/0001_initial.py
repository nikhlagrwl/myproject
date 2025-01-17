# Generated by Django 3.1.4 on 2020-12-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(db_column='User Id', primary_key=True, serialize=False)),
                ('email', models.EmailField(db_column='Email', max_length=128, unique=True)),
                ('first_name', models.CharField(db_column='First Name', max_length=25)),
                ('last_name', models.CharField(db_column='Last Name', max_length=25)),
                ('password', models.CharField(db_column='Password', max_length=256)),
                ('favourite', models.CharField(db_column='Favourite', default=None, max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='Created At')),
            ],
        ),
    ]
