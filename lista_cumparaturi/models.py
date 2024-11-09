from django.db import models

# Create your models here.

class Produs(models.Model):
    nume = models.CharField(max_length=255)
    cumparat = models.BooleanField(default=False)

    class Meta:
        verbose_name ='Produs'
        verbose_name_plural ='Produse'

    def __str__(self):
        return self.nume
