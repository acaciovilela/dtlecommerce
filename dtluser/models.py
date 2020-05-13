from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
