from django.db import models

# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    address=models.TextField(max_length=1000)
    city=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    state=models.CharField(max_length=200)
    pincode=models.IntegerField(max_length=200)
    phone=models.CharField(max_length=200)

    def __str__(self):
        return(f"{self.first_name}{self.last_name}")
