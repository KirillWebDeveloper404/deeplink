from django.db import models


class User(models.Model):
    tg_id = models.TextField()
    name = models.CharField(max_length=100, unique=False)
    phone = models.CharField(max_length=20, unique=True, blank=True)

    class Meta:
        verbose_name = 'User'


class Link(models.Model):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    ozon = models.CharField(max_length=1000, unique=False, null=True)
    wb = models.CharField(max_length=1000, unique=False, null=True)
    ali = models.CharField(max_length=1000, unique=False, null=True)
    ym = models.CharField(max_length=1000, unique=False, null=True)

    class Meta:
        verbose_name = 'Link'
