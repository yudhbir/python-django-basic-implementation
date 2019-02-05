from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Usermodel(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=254)
	created_on = models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = "tbl_users"
		
		