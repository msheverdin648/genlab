# Generated by Django 3.1 on 2021-03-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20210303_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='ФИО пользователя')),
                ('phone', models.CharField(max_length=150, verbose_name='Номер телефона')),
                ('research', models.CharField(max_length=255, verbose_name='Исследование')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
            ],
            options={
                'verbose_name': 'Заявка на исследование',
                'verbose_name_plural': 'Заявки на исследование',
            },
        ),
        migrations.CreateModel(
            name='UsersQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='ФИО пользователя')),
                ('phone', models.CharField(max_length=150, verbose_name='Номер телефона')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос пользователя',
                'verbose_name_plural': 'Вопросы пользователей',
            },
        ),
        migrations.AlterField(
            model_name='headerslid',
            name='page',
            field=models.CharField(choices=[('cooperation', 'Сотрудничество'), ('home', 'Главная страница'), ('news', 'Новости'), ('about', 'О нас'), ('questions', 'Как сдать анализы'), ('researches', 'Исследования')], default='home', max_length=50, verbose_name='Страница на которой отображать данный слайд'),
        ),
    ]
