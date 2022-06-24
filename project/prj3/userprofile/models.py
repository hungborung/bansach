from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.BooleanField(null=True, blank=True, default=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, default='static/user/profilepic.png', upload_to='static/user')

    def __str__(self):
        return self.username

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            if self.image:
                self.image = self.make_image(self.image)
                self.save()
                
                return self.image.url
            else:
                return ''