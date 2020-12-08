# Generated by Django 3.1 on 2020-12-08 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20201208_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerslid',
            name='page',
            field=models.CharField(choices=[('researches', 'Исследования'), ('questions', 'Как сдать анализы'), ('home', 'Главная страница'), ('cooperation', 'Сотрудничество')], default='home', max_length=50, verbose_name='Страница на которой отображать данный слайд'),
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.SlugField(verbose_name='Cсылка на новость'),
        ),
    ]
