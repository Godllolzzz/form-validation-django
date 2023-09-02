from django.db import models

# Create your models here.
class PracticeModel(models.Model):
    user_name = models.CharField(max_length=50)
    user_age = models.IntegerField()
    user_image = models.FileField(upload_to="images")
    # user_image = models.ImageFiFeld(upload_to="images")

    def __str__(self):
        return f"{self.user_name} - {self.user_age}"
