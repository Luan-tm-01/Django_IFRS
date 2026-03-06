from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True #Qnd eu quiser que todo modelo tenha algo, eh dentro dessa classe
        app_label = 'exemplo'
