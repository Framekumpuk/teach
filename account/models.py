from django.db import models

class Account(models.Model):
    account_text = models.CharField(max_length=200)
    account_money = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
