from django.db import models

class Blueprint(models.Model):
    name = models.CharField(max_length=200, blank=True, default="Blueprint")
    text = models.TextField()
    
    def __str__(self):
        return self.name