# Generated by Django 3.1 on 2020-10-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20201022_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headerslid',
            name='button_link',
        ),
        migrations.RemoveField(
            model_name='headerslid',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='headerslid',
            name='link_text',
        ),
        migrations.RemoveField(
            model_name='headerslid',
            name='link_url',
        ),
        migrations.AlterField(
            model_name='headerslid',
            name='page',
            field=models.CharField(choices=[('questions', 'Как сдать анализы'), ('researches', 'Исследования'), ('cooperation', 'Сотрудничество'), ('home', 'Главная страница')], default='home', max_length=50, verbose_name='Страница на которой отображать данный слайд'),
        ),
    ]