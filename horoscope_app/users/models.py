from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from .get_sign import return_sign
import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    birthday = models.DateField(default=datetime.date.today, null=True)
    # calculate sign here?
    sign = models.CharField(max_length=15, default='No sign', null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # if bday:
        #     user.profile.birthday = bday
        #     user.profile.sign = return_sign(bday)
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)