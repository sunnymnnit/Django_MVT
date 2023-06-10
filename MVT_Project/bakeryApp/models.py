from django.db import models

class BakeryCards(models.Model):
    cardId=models.IntegerField(default=0)
    title=models.TextField(max_length=100)
    description=models.TextField(max_length=300)
    image=models.TextField(max_length=600,default="")
    rate=models.IntegerField()

