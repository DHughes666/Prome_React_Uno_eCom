from django.db import models
from django.contrib.auth.models import AbstractUser

def get_profile_image_filepath(self, filename):
    return f'profile_image/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "prof_Ima/prof.png"

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(verbose_name='username', max_length=50, unique=True)
    
    

    # The field is already there, we have to make it as None because we're not
    # gogin to be sign in of the user based on the username
    #username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(verbose_name='address', max_length=255)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True,
                                                default=get_default_profile_image)

    # Django doesn't work wih token based so obviously the fields need to be
    # stored.
    session_token = models.CharField(max_length=10, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

