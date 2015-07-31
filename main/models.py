from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('main:company', args=(self.id,))

    def __unicode__(self):              # __unicode__ on Python 2
            return self.name

    class Meta:
        ordering = ('name',)


class Person(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('main:person', args=(self.id,))

    def __unicode__(self):              # __unicode__ on Python 2
            return self.name

    class Meta:
        ordering = ('name',)


class Platform(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('main:platform', args=(self.id,))

    def __unicode__(self):              # __unicode__ on Python 2
            return self.name

    class Meta:
        ordering = ('name',)


class ReleaseDate(models.Model):
    region = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)

    def __unicode__(self):              # __unicode__ on Python 2
            return self.region + ' ' + self.date.__str__()

    class Meta:
        ordering = ('date',)


class Genre(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('main:genre', args=(self.id,))

    def __unicode__(self):              # __unicode__ on Python 2
            return self.name

    class Meta:
        ordering = ('name',)


class Mode(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('main:mode', args=(self.id,))

    def __unicode__(self):              # __unicode__ on Python 2
            return self.name

    class Meta:
        ordering = ('name',)


class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    cover = models.ImageField(upload_to='covers', default='')
    developer = models.ManyToManyField(Company, related_name='%(app_label)s_%(class)s_developed')
    publisher = models.ManyToManyField(Company, related_name='%(app_label)s_%(class)s_published')
    designer = models.ManyToManyField(Person, related_name='%(app_label)s_%(class)s_designed')
    composer = models.ManyToManyField(Person, related_name='%(app_label)s_%(class)s_composed')
    platform = models.ManyToManyField(Platform, related_name='%(app_label)s_%(class)s')
    release_date = models.ManyToManyField(ReleaseDate, related_name='%(app_label)s_%(class)s')
    genre = models.ManyToManyField(Genre, related_name='%(app_label)s_%(class)s')
    mode = models.ManyToManyField(Mode, related_name='%(app_label)s_%(class)s')

    def get_absolute_url(self):
        return reverse('main:game', args=(self.id,))

    def __unicode__(self):              # __unicode__ on Python 2
            return self.name

    class Meta:
        ordering = ('name',)
