from django.db import models
from datetime import datetime
class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)

    def __str__(self):
        return self.name


class Board(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    category = models.CharField("Категория", max_length=255)
    description = models.TextField("Описание")
    image = models.CharField("URL изображения", max_length=500)
    price = models.IntegerField("Цена", null=True, blank=True)
    is_related_price = models.BooleanField("Цена", default=False, null=True, blank=True)
    author_name = models.CharField("Автор", max_length= 50)
    author_number = models.CharField("Номер телефона", max_length= 20)
    posted_date = models.DateTimeField("Дата и время публикации", default=datetime.now())

    def __str__(self):
        return self.title