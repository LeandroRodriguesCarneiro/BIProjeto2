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
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    na_sales = models.DecimalField(max_digits=10, decimal_places=2)
    eu_sales = models.DecimalField(max_digits=10, decimal_places=2)
    jp_sales = models.DecimalField(max_digits=10, decimal_places=2)
    other_sales = models.DecimalField(max_digits=10, decimal_places=2)
    global_sales = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name