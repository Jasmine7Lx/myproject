from django.db import models

# Create your models here.
class USER(models.Model):
    #user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    user_email = models.EmailField(unique=True)
    category = models.CharField(max_length=100, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name
'''
    class Meta:
        ordering = ['created_time']
        verbose_name = 'user'
'''
