from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(max_length=150)
    birthday = models.DateField()
    
    def __str__(self):   
        return self.name
        
    
class Category(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='products')
    
    def __str__(self):
        return self.name
    

class Players(models.Model):
    mane = models.CharField(max_length=100)
    games = models.ManyToManyField('Games', related_name="players_settings")
    
    def __str__(self):
        return self.name
    
class Games(models.Model):
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
    
class MyModel(models.Model):
    short_text = models.CharField(max_length=250)
    long_text = models.TextField()
    numder = models.IntegerField()
    float_numder = models.DecimalField(decimal_places=3, max_digits=10)
    date = models.DateField()
    date_time = models.DateTimeField(auto_now_add=True)
    related = models.ForeignKey(Games, related_name='one_to_many', on_delete=models.DO_NOTHING)
    many_to_many = models.ManyToManyField(Games, related_name = "many_to_many")
    true_or_false = models.BooleanField(default=False)
    
    