from django.shortcuts import HttpResponse 
from django.shortcuts import render
from django.shortcuts import redirect
import xlwt
import datetime
from collections import OrderedDict
# import pytz
from pages.models import Post
from .render import Rendering 

# Create your views here.
def home(request):	
	return render(request, 'pages/home.html', {'active': 'home'})
	
def about(request):	
	return render(request, 'pages/about.html', {'active': 'about'})
	
def contact(request):	
	return render(request, 'pages/contact.html', {'active': 'contact'})

def export_users_xls(request):
	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Post')

	# Sheet header, first row	
	
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	columns = ['Post Title', 'Post Description', 'Post Category','Created On']

	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
	font_style = xlwt.XFStyle()	
	rows = Post.objects.select_related('category').all()	#join with category model
	post_list=OrderedDict()
	i=0;
	for row in rows:
		# print row._meta.get_fields()
		post_list[i]=OrderedDict()
		post_list[i]['post_title']=row.post_title
		post_list[i]['post_description']=row.post_description
		post_list[i]['category']=row.category.category_name
		post_list[i]['created_on']=row.created_on.strftime("%Y-%m-%d %H:%M:%S")
		i+=1	
	# print len(post_list)
	for key, value in post_list.items():		
		row_num += 1		
		item= value.values()		
		for col in range(len(item)):
			ws.write(row_num, col, item[col], font_style)			
			
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="posts.xls"'
	wb.save(response)
	return response
	
def export_pdf(request):
	print 'hi'
	return Rendering.test()