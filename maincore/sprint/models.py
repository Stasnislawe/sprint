from django.db import models

# Create your models here.

class User(models.Model):
    """"Пользователи"""
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    phone = models.IntegerField(unique=True, verbose_name='Телефон')

    def __str__(self):
        return f'{self.pk}: {self.name} {self.surname}'

class Coords(models.Model):
    """"Координаты перевала"""
