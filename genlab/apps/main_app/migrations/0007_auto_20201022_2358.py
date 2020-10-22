# Generated by Django 3.1 on 2020-10-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20201022_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerslid',
            name='button_link',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ссылка кнопки'),
        ),
        migrations.AddField(
            model_name='headerslid',
            name='button_text',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Текст кнопки(если есть)'),
        ),
        migrations.AddField(
            model_name='headerslid',
            name='link_text',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Текст ссылки(если есть)'),
        ),
        migrations.AddField(
            model_name='headerslid',
            name='link_url',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='URL ссылки'),
        ),
        migrations.AlterField(
            model_name='headerslid',
            name='page',
            field=models.CharField(choices=[('cooperation', 'Сотрудничество'), ('questions', 'Как сдать анализы'), ('researches', 'Исследования'), ('home', 'Главная страница')], default='home', max_length=50, verbose_name='Страница на которой отображать данный слайд'),
        ),
    ]
