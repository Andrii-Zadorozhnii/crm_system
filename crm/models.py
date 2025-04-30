from datetime import datetime
from email.policy import default

from django.db import models
from django.db.models import CharField, BooleanField, DateTimeField, IntegerField, EmailField, CASCADE


# Create your models here.


class Clients(models.Model):
    name = CharField(max_length=30)
    email = EmailField()
    phone = CharField(max_length=30)
    company = CharField(max_length=30)

class Deals(models.Model):
    name = CharField(max_length=50)
    price = IntegerField()
    status = CharField(max_length=30)
    client = models.ForeignKey(to=Clients, on_delete=CASCADE)

class Tasks(models.Model):
    description = CharField(max_length=30)
    deadline =DateTimeField()
    comleted =BooleanField(default=False)
    client = models.ForeignKey(to=Clients, on_delete=CASCADE)

