from django.db import models
from dJango.contrib import admin
from .models import MenuCategory
admin.site.register(MenuCategory)

class MenuCategory(models.Model):
    name= models.CharFeild(max_length=100,unique=True)
    def __str__(self):
        return self.name
