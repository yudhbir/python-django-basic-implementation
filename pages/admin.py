from django.contrib import admin
from .models import Category,Post
from django.urls import reverse
from django.utils.html import format_html

#Custom function implementation
def mark_selected_category_active(self, request, queryset):	
	rows_updated = queryset.update(status='1')
	if rows_updated == 1:
		message_bit = "1 story was"
	else:
		message_bit = "%s stories were" % rows_updated
	self.message_user(request, "%s successfully marked as Active." % message_bit)	
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_name', 'status','created_on']
	list_filter = ['category_name', 'created_on']
	list_editable = ['category_name']
	list_display_links = None
    # prepopulated_fields = {'slug': ('name',)}
	actions = [mark_selected_category_active,]
	
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
	list_display = ['post_title','category_link', 'short_description','created_on','action']
	list_filter = ['post_title', 'created_on']
	list_editable = ['post_title']
	list_display_links = None
	def category_link(self, obj):
		link = reverse("admin:pages_category_change", args=[obj.category.id])
		return format_html('<a href="{}">{}</a>', link, obj.category.category_name)
	def action(self, obj):		
		url = reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.id] )		
		return format_html('<a href="{}">{}</a>', url, 'Edit')

admin.site.register(Post, PostAdmin)