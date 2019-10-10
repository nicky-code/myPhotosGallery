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
        pass
 
    def filter_by_location(location):
        pass   
    
    
class Location(models.Model):
    loc_name = models.CharField(max_length =50)
    images=models.OneToManyField(images)
    
    def __str__(self):
        return self.location

    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
        
    def update_location(self):
        self.update()
        
class Category(models.Model):
    cat_name=  models.CharField(max_length =50)
    images = models.ManyToManyField(images)
    

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
        
    def update_category(self):
        self.update()