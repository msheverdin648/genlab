# Generated by Django 3.1 on 2020-11-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20201027_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchmethod',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='Что исследуется'),
        ),
        migrations.AddField(
            model_name='researchmethod',
            name='decryption',
            field=models.TextField(blank=True, null=True, verbose_name='Расшифровка'),
        ),
        migrations.AddField(
            model_name='researchmethod',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание исследования'),
        ),
        migrations.AddField(
            model_name='researchmethod',
            name='preparation',
            field=models.TextField(blank=True, null=True, verbose_name='Подготовка'),
        ),
        migrations.AlterField(
            model_name='headerslid',
            name='page',
            field=models.CharField(choices=[('researches', 'Исследования'), ('questions', 'Как сдать анализы'), ('home', 'Главная страница'), ('cooperation', 'Сотрудничество')], default='home', max_length=50, verbose_name='Страница на которой отображать данный слайд'),
        ),
    ]