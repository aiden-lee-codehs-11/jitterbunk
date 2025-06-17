
# Create your models here.
"""

### 1. **Create Models**

- Resource
    - title
    - notion link
    - date of training
    - who ran it
    - team (string)
- User (optionally, you could use the Django auth user model! but make your own first!)
    - username (string)
    - photo (string)
    - team (string)
"""

import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    team = models.CharField(max_length=200)

class Resource(models.Model):
    title = models.CharField(max_length=200)
    notion_link = models.CharField(max_length=200)
    training_date = models.DateTimeField('date of training')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.CharField(max_length=200)
