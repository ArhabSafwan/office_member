from django.db import models

from django.db import models

class Member_api(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)