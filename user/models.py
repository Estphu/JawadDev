from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# User Profile Model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=60, null=True)
    avatar = models.ImageField(default='user/avatars/default_avatar.jpg', upload_to="user/avatars/")
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    address = models.CharField(max_length=60, null=True)
    bio = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.get_username())
        super().save(*args, **kwargs)  

        # img = Image.open(self.avatar.path) # Open image

        # # resize image
        # if img.height > 500 or img.width > 500:
        #     output_size = (500, 500)
        #     img.thumbnail(output_size) # Resize image
        #     img.save(self.avatar.path) # Save it again and override the larger image