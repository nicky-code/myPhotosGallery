from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.

class ImageTestClass(TestCase):
    '''
    a class to test the image instances and its methods
    '''

    # Set up method
    def setUp(self):
        self.nicky= Image(image='images/',image_name='photo', image_description='sitting')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nicky,Image))
    
    # Testing Save Method
    def test_save_method(self):
        '''
        function to check the save method of image
        '''
        self.nicky.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
        
    def test_delete_image(self):
        '''
        a method to delete a saved image
        '''
        self.nicky.save_image()
        picture = Image.objects.filter(image_name='photo').first()
        delete = Image.objects.filter(image_name=picture.image_name).delete()
        image=Image.objects.all()
        self.assertFalse(len(image)==1)
        
    def test_update_image(self):
        '''
        a method that helps to update the image
        '''
        self.nicky.save_image()
        picture= Image.objects.filter(image_name='photo').first()
        update = Image.objects.filter(image_name=picture.image_name).update(image_name='pic')
        updated = Image.objects.filter(image_name='pic').first()
        self.assertNotEqual(picture.image_name,updated.image_name)
    
    
class LocationTestClass(TestCase):
    '''
    a class to test the location instances and its methods
    '''
    
    # Set up method
    def setUp(self):
        self.nicky= Location(location_image='Kimihurura')
        

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nicky, Location))
    
    # Testing Save Method
    def test_save_location(self):
        '''
        function to check the save method of location
        '''
        self.nicky.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
        
    def test_delete_location(self):
        '''
        a method to delete a saved location
        '''
        self.nicky.save_location()
        picture = Location.objects.filter(location_image='Kimihurura').first()
        delete = Location.objects.filter(location_image=picture.location_image).delete()
        location=Location.objects.all()
        self.assertFalse(len(location)==1)
        
    def test_update_location(self):
        '''
        a method that helps to update the location
        '''
        self.nicky.save_location()
        picture = Location.objects.filter(location_image='Kimihurura').first()
        update = Location.objects.filter(location_image=picture.location_image).update(location_image='Kimironko')
        updated = Location.objects.filter(location_image='Kimironko').first()
        self.assertNotEqual(picture.location_image,updated.location_image)
    
    
    
class CategoryTestClass(TestCase):
    '''
    a class to test the category instances and its methods
    '''
    
    # Set up method
    def setUp(self):
        self.nicky= Category(cat_name='Fashion')
        

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nicky,Category))
    
    # # Testing Save Method
    # def test_save_location(self):
    #     '''
    #     function to check the save method of location
    #     '''
    #     self.nicky.save_location()
    #     locations = Location.objects.all()
    #     self.assertTrue(len(locations) > 0)
        
    # def test_delete_location(self):
    #     '''
    #     a method to delete a saved location
    #     '''
    #     self.nicky.save_location()
    #     picture = Location.objects.filter(location_image='Kimihurura').first()
    #     delete = Location.objects.filter(location_image=picture.location_image).delete()
    #     location=Location.objects.all()
    #     self.assertFalse(len(location)==1)
        
    # def test_update_location(self):
    #     '''
    #     a method that helps to update the location
    #     '''
    #     self.nicky.save_location()
    #     picture = Location.objects.filter(location_image='Kimihurura').first()
    #     update = Location.objects.filter(location_image=picture.location_image).update(location_image='Kimironko')
    #     updated = Location.objects.filter(location_image='Kimironko').first()
    #     self.assertNotEqual(picture.location_image,updated.location_image)
    