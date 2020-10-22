from django.db import models



class ResearchMethod(models.Model):

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Метод исследования'
        verbose_name_plural = 'Методы исследования'
    
    name = models.CharField(("Название метода"), max_length=500)
    period = models.IntegerField(("Срок исследования"))
    price = models.DecimalField(("Цена исследования"), max_digits=12, decimal_places=2)
    slug = models.SlugField(("Ссылка метода"))


    def __str__(self):
        return self.name
    


class ResearchType(models.Model):

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Вид исследования'
        verbose_name_plural = 'Виды исследования'
    
    name = models.CharField(("Название вида исследования"), max_length=500)
    methods = models.ManyToManyField(ResearchMethod, verbose_name=("Методы исследования"))

    def __str__(self):
        return self.name

class Research(models.Model):

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Исследование'
        verbose_name_plural = 'Исследования'

    name = models.CharField(("Название исследования"), max_length=150)
    types = models.ManyToManyField(ResearchType, verbose_name=("Входящие в него виды исследвания"))


    def __str__(self):
        return self.name



class MainResearches(models.Model):

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Основное направление исследования'
        verbose_name_plural = 'Основные направления исследования'

    name = models.CharField(("Название основного направления"), max_length=256)
    types = models.ManyToManyField(ResearchType, verbose_name=("Методы исследования данного направления"))  

    def __str__(self):
        return self.name


class HeaderSlid(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Слайд хедера'
        verbose_name_plural = 'Слайды хедера'


    HOME = 'home'
    RESEARCHES = 'researches'
    QUESTIONS = 'questions'
    COOPERATION = 'cooperation'

    CHOICE_GROUP = {
        (HOME, 'Главная страница'),
        (RESEARCHES, 'Исследования'),
        (QUESTIONS, 'Как сдать анализы'),
        (COOPERATION, 'Сотрудничество'),
    } 

    slide_header = models.CharField(("Заголовок слайда"), max_length=500)
    slide_text = models.TextField(("Текст слайда"))
    page = models.CharField(("Страница на которой отображать данный слайд"), choices=CHOICE_GROUP, default=HOME,  max_length=50)
    image = models.ImageField(("Фото отобржаемое на слайдере"), upload_to='img', null=True, blank=True)
    button_text = models.CharField(("Текст кнопки(если есть)"), max_length=50, null=True, blank=True)
    button_link = models.CharField(("Ссылка кнопки"), max_length=50 , null=True, blank=True)
    link_text = models.CharField(("Текст ссылки(если есть)"), max_length=50, null=True, blank=True)
    link_url = models.CharField(("URL ссылки"), max_length=50 , null=True, blank=True)

    def __str__(self):
        return self.slide_header+ f'({self.page})'


class QuestionsAnswers(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Часто задаваемый вопрос/ответ'
        verbose_name_plural = 'Часто задаваемые вопросы/ответы'

    question = models.CharField(("Вопрос"), max_length=500)
    answer = models.TextField(("Ответ"))
    show_home = models.BooleanField(("Отображение на главной странице"))

    def __str__(self):
        return self.question

class About(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Карточка блока подробнее о нас'
        verbose_name_plural = 'Карточки блока подробнее о нас'

    name = models.CharField(("Заголовок карточки"), max_length=150)
    short_text = models.CharField(("Краткое описание"), max_length=500)
    full_text = models.TextField(("Полное описание(без краткого)"))
    ico = models.FileField(("Иконка данного блока(jpg, svg, png)"), upload_to='img', max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

class Partners(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    name = models.CharField(("Название партнера"), max_length=256)
    img = models.ImageField(("Картинка логотипа"), upload_to='img')
    link = models.CharField(("Ссылка на сайт партнера"), max_length=256, null=True, blank=True)
    
    def __str__(self):
        return self.name

class News(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField(("Заголовок новости"), max_length=256)
    text = models.TextField(("Текст новости"))
    img = models.ImageField(("Картинка новости"), upload_to='img')
    date = models.DateField(("Дата новости"), auto_now=False, auto_now_add=False)
    link = models.CharField(("Ссылка на новость"), max_length=256)

    def __str__(self):
        return self.title

