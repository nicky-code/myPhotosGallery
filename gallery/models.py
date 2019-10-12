from django.db import models

# Create your models here.


class Location(models.Model):
    location_image = models.CharField(max_length =50)
    
    def __str__(self):
        return self.location_image

    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
        
    def update_location(self):
        self.update()
        
class Category(models.Model):
    cat_name=  models.CharField(max_length =50)
    

    def __str__(self):
        return self.cat_name

    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
        
    def update_category(self):
        self.update()
        
        
class Image(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    image_name = models.CharField(max_length =50)
    image_description = models.CharField(max_length =50)
    location = models.ForeignKey(Location, null=True)
    category= models.ForeignKey(Category, null=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_image(self):
        self.update()
        
    @classmethod    
    def get_image_by_id(cls,id):
        images = cls.objects.filter(id = id)
        return images
    @classmethod
    def search_image(cls,search_category):
        picture = cls.objects.filter(category__cat_name__icontains = search_category)
        return picture
    
    @classmethod
    def filter_by_location(cls,location):
        image = cls.objects.filter(location__location_image__icontains=location)
        return image
        
        
