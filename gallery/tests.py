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
        
    def test_update_image():
        '''
        a method that helps to update the image
        '''
        self.nicky.save_image
        picture= Image.objects.filter(image_name='photo').first()
        update = Image.