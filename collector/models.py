from django.db import models

class Submission(models.Model):
    height_m = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Height (meters)")
    front_photo = models.ImageField(upload_to='photos/%Y/%m/%d/front/')
    side_photo = models.ImageField(upload_to='photos/%Y/%m/%d/side/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.id} - {self.height_m}m"
