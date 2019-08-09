# Generated by Django 2.2.3 on 2019-08-09 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesApp', '0007_game_on_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('m_email', models.EmailField(max_length=254)),
                ('m_birthday', models.DateField(verbose_name='birthday')),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]