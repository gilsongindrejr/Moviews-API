from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    name = models.CharField(_('name'), max_length=100)
    release_date = models.DateField(_('release date'))
    director = models.CharField(_('director'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
