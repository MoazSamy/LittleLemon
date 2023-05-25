from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()
    
    # For tests
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
    # For Admin Dashboard
    def __str__ (self):
        return f'{self.title} : {str(self.price)}'