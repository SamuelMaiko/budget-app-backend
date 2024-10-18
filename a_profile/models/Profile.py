from django.db import models
from a_shared.models import BaseModel
from django.conf import settings

class Profile(BaseModel):
    profile_picture = models.ImageField(upload_to='profile_pictures/',default="profile_pictures/default.jpg", blank=True, null=True)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="profile")

    class Meta:
        db_table = "profiles"  
    def __str__(self):
        return f'Profile of {self.user.username}'