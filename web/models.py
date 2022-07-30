from django.db import models
import datetime
# Create your models here.
class Contact(models.Model):
      phone = models.IntegerField(null =True)
      email = models.EmailField(max_length= 122,null = True)
      query = models.TextField(max_length= 200,unique = True,null = True)
      answer = models.TextField(max_length = 200,null = True)
      create_time = models.DateTimeField(auto_now_add=True,null =True)
      update_time = models.DateTimeField(auto_now=True)
      def __str__(self):
           return self.query
