from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Movie(models.Model):
    name = models.CharField(_('name'), max_length=100)
    release_date = models.DateField(_('release date'))
    director = models.CharField(_('director'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class Rating(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_('user'), on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, verbose_name=_('movie'), on_delete=models.CASCADE, related_name='ratings')
    title = models.CharField(_('title'), max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField(_('comment'), max_length=255)

    def __str__(self):
        return f'{self.user} rated {self.rating} on movie {self.movie}'
