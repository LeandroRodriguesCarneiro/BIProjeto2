from django.db import models

class Genre(models.Model):
    genre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.genre

class Platform(models.Model):
    platform = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.platform

class Publisher(models.Model):
    publisher = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.publisher

class Game(models.Model):
    name = models.CharField(max_length=255)
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING)
    year = models.IntegerField(null=True)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    na_sales = models.FloatField()
    eu_sales = models.FloatField()
    jp_sales = models.FloatField()
    other_sales = models.FloatField()
    global_sales = models.FloatField()
    def __str__(self):
        return self.name