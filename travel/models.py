from django.db import models


class Destination(models.Model):
    name  = models.CharField(max_length = 150)
    img  = models.ImageField(upload_to='pics') 
    desc = models.TextField()
    price = models.IntegerField()

    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'

    def __str__(self):
        return self.name    
    

class Packages(models.Model):
    name = models.CharField(max_length=100) 
    price = models.IntegerField()
    PackagesDesc = models.TextField()
    accomodation = models.CharField(max_length = 150)
    traspotation = models.CharField(max_length = 150)
    foodFacility = models.CharField(max_length = 150)
    reviewNumbers = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer  = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Packages' #admin area name
        # ordering = ('-created',) #order in descending of being updated

    def __str__(self):
        return self.name 
         
