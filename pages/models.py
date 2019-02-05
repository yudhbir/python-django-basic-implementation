from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import truncatechars

# Create your models here.
class Category(models.Model):
	GENDER_CHOICES = (
        ('1', 'Active'),
        ('0', 'Inactive'),
    )
	category_name = models.CharField(max_length=100)		
	status = models.CharField(max_length=1,choices=GENDER_CHOICES,default='0')		
	created_on = models.DateTimeField(auto_now_add=True)	
	class Meta:
		db_table = "tbl_category"
	# if you want that category showing its name rather than its name in the another models where it is act like foreign key
	def __str__(self):
		return self.category_name
		
class Post(models.Model):
	post_title = models.CharField(max_length=200)
	post_description = models.TextField(blank=True, null=True)	
	created_on = models.DateTimeField(auto_now_add=True)
	update_on = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(to=Category, related_name="Category", null=True, blank=True)
	class Meta:
		db_table = "tbl_posts"
	# Change the property of the model w.r.t show in another sections.(e.g. admin)
	@property
	def short_description(self):
		return truncatechars(self.post_description, 40)
		
class SubCategory(models.Model):
	category_name = models.CharField(max_length=100)		
	created_on = models.DateTimeField(auto_now_add=True)
	parent_category = models.ForeignKey(to=Category, related_name="ParentCategory", null=True, blank=True)
	class Meta:
		db_table = "tbl_subcategory"
