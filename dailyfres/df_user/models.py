# coding=utf-8
from django.db import models

# Create your models here.


class Passport(models.Model):
    username = models.CharField(max_length=20)
    passpowd = models.CharField(max_length=40)

    def __str__(self):
        return "%s" % self.pk
