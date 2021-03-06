# coding: utf-8
#python 2:
from __future__ import unicode_literals, absolute_import, print_function
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name).encode('ascii', errors='replace')

class Publisher(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author')
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey('Publisher')

    def __str__(self):
        return self.title
