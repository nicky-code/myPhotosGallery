from django.db import models

# Create your models here.
class Image(models.Model):
    id = models.CharField
    image = models.ImageField(upload_to='/')
    image_name = models.CharField(max_length =50)
    image_description = models.CharField(max_length =50)
    location=models.foreignKey(Location)
    category=models.foreignKey(Category)
    
    def __str__(self):
        return self.image

    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_image(self):
        self.update()
        
    def get_image_by_id(id):
        pass
    
    def search_image(cls,category):
        
    
    
    
class Location(models.Model):
    loc_name = models.CharField(max_length =50)
    images=models.OneToManyField(images)
    
    
class Category(models.Model):
    cat_name=  models.CharField(max_length =50)
    images = models.ManyToManyField(images)
    