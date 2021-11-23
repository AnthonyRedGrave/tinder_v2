# Generated by Django 3.2.9 on 2021-11-23 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favorites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('russian', 'Русский'), ('english', 'Английский'), ('belarussian', 'Беларусский'), ('francian', 'Французский'), ('italian', 'Итальянский')], max_length=15, verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('default', 'Обычный'), ('premium', 'Премиум'), ('vip', 'Вип')], max_length=15, verbose_name='Статус профиля')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='ProfileInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], max_length=20, verbose_name='Пол')),
                ('education', models.CharField(choices=[('higher', 'Высшее'), ('secondary', 'Среднее'), ('school', 'Школьное')], max_length=30, verbose_name='Образование')),
                ('weight', models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Вес')),
                ('description', models.TextField(verbose_name='Описание профиля')),
                ('location', models.CharField(max_length=150, verbose_name='Место расположения')),
                ('registration_date', models.DateTimeField(auto_now=True, verbose_name='Дата регистрации профиля')),
                ('favorites', models.ManyToManyField(related_name='profile_information', to='favorites.Favorites')),
                ('languages', models.ManyToManyField(to='profiles.Language', verbose_name='Языки')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_information', to='profiles.profile')),
            ],
            options={
                'verbose_name': 'Информация о профиле',
                'verbose_name_plural': 'Информации о профилях',
            },
        ),
    ]
