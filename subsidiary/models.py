from django.db import models


class Subsidiaryies(models.Model):
    count_halls = models.IntegerField()
    describe = models.TextField(blank=True)
    address = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return 'Описание: ' + self.describe
