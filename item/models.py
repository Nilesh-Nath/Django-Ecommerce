from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length = 255)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    

class items(models.Model):
    category = models.ForeignKey(categories,related_name="item",on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    description = models.TextField(null=True, blank = True)
    price = models.FloatField()
    image = models.ImageField(upload_to="item_images",blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name="item",on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Items"
        
    def __str__(self):
        return self.name