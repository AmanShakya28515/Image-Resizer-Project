from django.db import models

class ImageResize(models.Model):
    image = models.ImageField(upload_to='images/') #The ImageField column in your database will store the relative path to the image file (e.g., images/your_uploaded_image.jpg).
    resize_percentage = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.image.name} ({self.resize_percentage}%)"
  


