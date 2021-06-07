from django.db import models


class Style(models.Model):
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='styles/images')
    image = models.ImageField(upload_to='media/', blank=True)
    model = models.FileField(upload_to='styles/models')

    def __str__(self):
        return str(self.name)


# https://res.cloudinary.com/hlve30y0w/image/upload/v1622874819/media/afermov_fdhry3.jpg
