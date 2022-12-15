from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
#from django.contrib.auth import get_user, get_user_model
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
     username = models.CharField(verbose_name='ユーザー名', max_length=10, unique=True)
     email = models.EmailField(verbose_name='メールアドレス',unique=True)
     image = models.ImageField(verbose_name='画像', upload_to="image/",default="")
     def __str__(self):
          return self.username
     
#User = get_user_model()
class Message(models.Model):
     name_from = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="name_from")
     name_to = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="name_to")
     content = models.CharField(max_length=300)
     create_at = models.DateTimeField(default = timezone.now)
     def __str__(self):
          return str(self.name_from)

