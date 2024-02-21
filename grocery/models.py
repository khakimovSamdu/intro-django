from django.db import models

# Create your models here.
class Backend(models.Model):
    name = models.TextField()
    price = models.TextField()
    quantity = models.TextField()
    char_text = models.CharField(max_length = 8, blank = True)

    def __str__(self) -> str:
        return self.name +"  " + self.price + "  " + self.quantity

class Frontend(models.Model):
    name = models.TextField()
    price = models.TextField()
    quantity = models.TextField()
    
    def __str__(self) -> str:
        return self.name + "  " + self.price + "  " + self.quantity
