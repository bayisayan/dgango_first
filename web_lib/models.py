from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=200)
    age = models.PositiveIntegerField(verbose_name='Возраст')
    e-mail = models.EmailField()
    lit_type()