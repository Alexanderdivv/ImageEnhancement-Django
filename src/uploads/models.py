from django.db import models
from .utils import get_filtered_image
from PIL import Image
import numpy as np
import os
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
ACTION_CHOICES= (
    ('NO_FILTER', 'no filter'),
    ('NEGATIVE', 'negative'),
    ('GREYSCALE', 'greyscale'),
    ('BRIGHTENING', 'brightening'),
    ('ARITMETIKA', 'aritmetika'),
    ('BOOLEAN', 'boolean'),
    ('GEOMETRI', 'geometri'),
)

class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images', blank=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        
        #open images
        pil_img = Image.open(self.image)
        pil_img2 = Image.open(self.image2)
       
        #convert the image to array and do sime processing
        cv_img = np.array(pil_img)
        cv_img = cv_img.astype('uint8')
        cv_img2 = np.array(pil_img2)
        cv_img2 = cv_img2.astype('uint8')
        img = get_filtered_image(cv_img, cv_img2, self.action)

        #stackoverflow
        
        #convert back to pil image
        im_pil = Image.fromarray(img)

        #save
        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)
