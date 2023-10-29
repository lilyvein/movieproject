import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import (MinLengthValidator, MinValueValidator, MaxValueValidator)


class Country (models.Model):
    common = models.CharField(max_length=100)
    official = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, null=True, blank=True)  # true ja blank on vajalik et kui andmevälio on tühi või o
    flag = models.CharField(max_length=255)
    map = models.CharField(max_length=255)

    def country_info(self):
        """ Country search """
        return f'{self.common}, {self.official}'

    def __str__(self):
        """ Admin page show info """
        return self.common

    class Meta:
        """ Default result ordering """
        ordering = ['common']
        verbose_name_plural = 'countries'


class Movie (models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    imdbID = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    poster = models.CharField(max_length=100, null=True, blank=True)

    def country_info(self):
        """ Country search """
        return f'{self.title}, {self.year}'

    class Meta:
        """ Default result ordering """
        ordering = ['title']
        verbose_name_plural = 'movies'

    def __str__(self):
        """ Admin page show info """
        return self.title

