from django.contrib import admin
from .models import Usermodel

class UsersAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email', 'created_on']
	list_filter = ['first_name', 'last_name', 'email', 'created_on']
	list_editable = ['first_name', 'last_name', 'email']
	list_display_links = None
    # prepopulated_fields = {'slug': ('name',)}

admin.site.register(Usermodel, UsersAdmin)


# Register your models here.
