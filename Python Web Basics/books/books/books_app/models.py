from django.core.validators import MinValueValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)


class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    description = models.CharField(max_length=100, default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)





