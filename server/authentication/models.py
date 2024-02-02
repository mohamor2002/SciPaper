from django.db import models
from django.contrib.auth.models import User
from papers.models import paper
# Create your models here.

class BasicUser(models.Model):
    """
    a user with simple privileges that includes:viewing and adding scientific documents to favourites.
    related by a many to many association to :model:`papers.paper`
    """ 
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choices = [
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE")
    ]
    gender = models.CharField(max_length=50, choices=choices)
    favorites = models.ManyToManyField(paper, blank = True)
    
    
    def __str__(self):
        return self.user.username
    

    
class moderator(models.Model):
    """
    a user with increased privileges that includes:viewing and modifying scientific documents,
    """ 
    
    class Meta:
        verbose_name = "moderator"
        verbose_name_plural = "moderators"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choices = [
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE")
    ]
    gender = models.CharField(max_length=50, choices=choices)
    
    
    def __str__(self):
        return self.user.username
    
    
    
class admin(models.Model):
    """
    a user with super privileges that includes:viewing,adding and removing scientific documents, viewing and removing users.
    """ 
    class Meta:
        verbose_name = "admin"
        verbose_name_plural = "admins"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choices = [
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE")
    ]
    gender = models.CharField(max_length=50, choices=choices)
    
    
    def __str__(self):
        return self.user.username