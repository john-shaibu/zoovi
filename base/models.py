from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.
class User(AbstractUser):
      first_name = models.CharField(max_length=30)
      last_name = models.CharField(max_length=30)
      email = models.EmailField(max_length=30, unique=True, null=True)
      password = models.CharField(max_length=60)

      # USERNAME_FIELD = 'email'
      # REQUIRED_FIELDS = []

      def __str__(self):
          return f'{self.first_name}, {self.last_name}'

class Video(models.Model):
      video = models.FileField(upload_to='videos/%y')
      video_owner = models.ForeignKey(User, on_delete=models.CASCADE)
      date_uploaded = models.DateTimeField(auto_now_add=True)


      def _str_(self):
            return f'{self.video}, {self.date_uploaded}'