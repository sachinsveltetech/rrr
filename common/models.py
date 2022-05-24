from django.db import models

# Create your models here.


class Tsp(models.Model):
    name=models.CharField(max_length=200)
    
    class Meta:
        ordering =['id']
        
    def __str__(self):
        return self.name
    
    
class State(models.Model):    
    name=models.CharField(max_length=200)
    
    class Meta:
        ordering=['id']
    
    def __str__(self) -> str:
        return self.name

class District(models.Model):
    name=models.CharField(max_length=200)
    # state=models.CharField(max_length=200,default='ASSAM')
    
    class Meta:
        ordering=['id']
    
    def __str__(self) -> str:
        return self.name
