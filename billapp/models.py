from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    foodname = models.CharField(max_length=20)
    quantity = models.IntegerField()
    cost = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='%y/%m/%d', default='')
    bills = models.ManyToManyField('Bill', through='BillOrders')
    def __str__(self):
        return self.foodname



class Bill(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    bdate = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=50, default='')
    foods = models.ManyToManyField('Food' , through='BillOrders')
    
    def total_price(self):
        queryset = self.foods.all().aggregate(
        total_price=models.Sum('cost'))
        return queryset["total_price"]
    

class BillOrders(models.Model):
    order = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='foods')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='bills')