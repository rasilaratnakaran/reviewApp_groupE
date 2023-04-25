from django.db import models
 
# Create your models here.
class user(models.Model):
	FirstName = models.CharField(max_length=255)
	LastName = models.CharField(max_length=255)
	DOB = models.DateField()
	Phone = models.IntegerField()
	email = models.EmailField()
	Address = models.CharField(max_length=255)
	City = models.CharField(max_length=255)
	Country = models.CharField(max_length=255)
	ZipCode = models.CharField(max_length=255)
	Password = models.CharField(max_length=255)
	Image = models.CharField(max_length=255)
	
 
def __str__(self):
    	return self.FirstName
