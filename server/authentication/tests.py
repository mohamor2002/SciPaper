from django.test import TestCase
from .models import BasicUser, moderator, admin
from django.contrib.auth.models import User

# Create your tests here.


class BasicUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        first_name = "zoubir"
        last_name = "akrem"
        username = "zoubir"
        password = "123"
        gender = "MALE"
        email = "zoubir@gmail.com"
# Set up non-modified objects used by all test methods
        user = User.objects.create(first_name = first_name,last_name =  last_name,username =  username,email = email,password = password)
        BasicUser.objects.create(user = user, gender = gender)
        
    def test_object_favourites_is_empty(self):
        user = BasicUser.objects.get(id = 1).user
        favourites = user.favorites
        self.assertTrue(favourites.isempty())
        
    def test_object_name(self):
        user = BasicUser.objects.get(id = 1).user
        name = f'{user.first_name} {user.last_name}'
        self.assertEqual(name, f'{first_name} {last_name}')
        
    def test_object_gender(self):
        user = BasicUser.objects.get(id = 1)
        self.assertEqual(user.gender, gender)

class moderatorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        first_name = "zoubir"
        last_name = "akrem"
        username = "zoubir"
        password = "123"
        gender = "MALE"
        email = "zoubir@gmail.com"
        
        # Set up non-modified objects used by all test methods
        user = User.objects.create(first_name = first_name,last_name =  last_name,username =  username,email = email,password = password)
        moderator.objects.create(user = user, gender = gender)
        
        
    def test_object_name(self):
        user = BasicUser.objects.get(id = 1).user
        name = f'{user.first_name} {user.last_name}'
        self.assertEqual(name, f'{first_name} {last_name}')
        
    def test_object_gender(self):
        user = BasicUser.objects.get(id = 1)
        self.assertEqual(user.gender, gender)

class adminModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        first_name = "zoubir"
        last_name = "akrem"
        username = "zoubir"
        password = "123"
        gender = "MALE"
        email = "zoubir@gmail.com" 
        # Set up non-modified objects used by all test methods
        user = User.objects.create(first_name = first_name,last_name =  last_name,username =  username,email = email,password = password)
        admin.objects.create(user = user, gender = gender)
        
        
    def test_object_name(self):
        user = BasicUser.objects.get(id = 1).user
        name = f'{user.first_name} {user.last_name}'
        self.assertEqual(name, f'{first_name} {last_name}')
        
    def test_object_gender(self):
        user = BasicUser.objects.get(id = 1)
        self.assertEqual(user.gender, gender)

