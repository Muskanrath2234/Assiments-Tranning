from django.db import models

# Create your models here.


class Blog(models.Model):
    Given_Input = models.CharField(null=False,max_length=300)
    result = models.TextField()

    def __str__(self):
        return self.topic
    
