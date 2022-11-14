from datetime import datetime

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=datetime(1970, 1, 1))

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

