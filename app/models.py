from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.TextField(verbose_name=u"Имя тега")



class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    upload = models.ImageField(upload_to='uploads/', default='static/img/unnamed.jpg')
    


class Question(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")
    tags = models.ManyToManyField(Tag)

    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания вопроса")

    is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']



class Answer(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField(verbose_name=u"Ответ на вопрос")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания ответа")

    is_active = models.BooleanField(default=True, verbose_name=u"Доступность ответа")

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ['-create_date']


class questionLike(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    current_state = models.NullBooleanField(verbose_name=u"Состояние лайка")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class answerLike(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    current_state = models.NullBooleanField(verbose_name=u"Состояние лайка")
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)