from django.db import models
class Restaurent(models.Model):
    name= models.CharField(max_length=200)
    adress = models.TextField()
  has_delivery = models.BooleanField(default=False)

  def __ str __(self):
    return self.name
