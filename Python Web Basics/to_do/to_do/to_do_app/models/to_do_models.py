from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name_plural = 'people'


class Category(models.Model):
    HOME_CHOICE = 'home'
    WORK_CHOICE = 'work'
    LEISURE_CHOICE = 'leisure'
    NAME_CHOICES = (
        (HOME_CHOICE, 'Home_stuff'),
        (WORK_CHOICE, 'Work_stuff'),
        (LEISURE_CHOICE, 'Leisure_stuff')
    )
    name = models.CharField(max_length=20, choices=NAME_CHOICES)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name_plural = 'categories'


class ToDo(models.Model):
    text = models.CharField(max_length=30)
    state = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True
    )
    categories = models.ManyToManyField(Category)


