# Gallery
## Gallery-App, 12th of October 2019
### By Aline Nicole UWAMARIYA
## Description
Galeery-App is a web application of the gallery of photos, that allows user to views different photos that interest him/her,search for different categories and views photos based on the location they were taken. 

## Code scaffolding
Run python3.6 manage.py runserver when you want to implement the features of the landing pages and other pages.

## BDD
### Behaviour
We want our application to:

1.View different photos that interest me.
2.Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
3.Search for different categories of photos. (ie. Travel, Food)
4.Copy a link to the photo to share with my friends.
5.View photos based on the location they were taken.

## Input Examples
1.search photos regarding their categories.
2.choose a location name and be able to view all the photos from that location.

## Output Examples
User will be able to see the photos he/she has searched for or chosen in location.

## TDD
I test my project using Python3.6 manage.py test gallery(my app-name).

## Setup/Installation Requirements
1.Your application should have a clean, simple, well-organized user interface. Ensure you choose a consistent color scheme and use appropriate fonts for your application. Also, you MUST create a mockup design for your application before you begin development.

2.Your Project must contain an Image model with the following properties:
a.Image
b.Image Name.
c.Image Description.
d.Image Location Foreign Key.
e.Image category Foreign Key.

3.Your Project must contain location and category that link to the Image model. Remember to make migrations to your database when you change the properties of the model.

4.Your Image model must contain the following methods:

a.save_image() - Save an image to the database.
b.delete_image() - Delete image from the database.
c.update_image() - Update image in the database.
d.get_image_by_id(id) - Allows us to get an image using its ID.
e.search_image(category) - Allows us to search for an image using its category.
f.filter_by_location(location) - Allows us to filter images by the location.

5.You should write tests for each of these methods and make sure you implement error handlers to prevent your application from crashing.

6.You must implement the save, update and delete methods in both models and make sure you write tests for each method

7.Your project must have a search form that when submitted calls a search function in the view function and redirects to a search results page.

8.When a user clicks on an Image he/she should be redirected where a larger version of the image is displayed and should also see the details of the Image.

9.A user should be able to click a button and have the link to the image copied to the machine’s clipboard. Make sure you write a test for this functionality.

10.Your project should have a dashboard that you will use to post photos to the database and manage the photos.

11.Your project should be deployed to Heroku when you have finished with the set features. You should provide the link to your project in the description part of your project repository.

## Technology used
Python3.6
Django
Heroku
Bootstrap4

## My link repository

## Contact me on aline.nicole7@gmail.com
## Title Licence
Copyright(c)2019 Aline Nicole UWAMARIYA



