import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
# handle URLs
# function based view
# def home_old(request):
# 	# put f string in the html: string substitution
# 	html_var = 'f strings'
# 	html_ = f"""
# 	<!DOCTYPE html>
# 	<html lang="en">
#   	<head>
#   	</head>
#   	<body>
#   	<h1>Hello World!</h1>
#   	<p>This is {html_var} coming through</p>
#   	</body>
#   	</html>
# 	""" # use triple " because it is a long string
# 	# f strings in Python 3: to do string substitution
# 	return HttpResponse(html_)
# 	#return render(request, "home.html", {}) #three args: req, template(jump to), context of the template #response

def home(request):
	num = None
	# some_list = [num, random.randint(0, 10000000), random.randint(0, 10000000)]
	some_list = [
		random.randint(0, 10000000), 
		random.randint(0, 10000000), 
		random.randint(0, 10000000)
	]
	# logic in the view itself, not so much in the template
	condition_bool_item = True
	if condition_bool_item:
		num = random.randint(0, 10000000)
	context = {
		# "bool_item": True, 
		"num": num, 
		"some_list": some_list
	}
	# return render(request, "base.html", {"html_var": "context variable"})
	return render(request, "home.html", context) # replace the context variable in the html/template

def about(request):
	context = {
	}
	# return render(request, "base.html", {"html_var": "context variable"})
	return render(request, "about.html", context) # replace the context variable in the html/template

def contact(request):
	context = {
	}
	# return render(request, "base.html", {"html_var": "context variable"})
	return render(request, "contact.html", context) # replace the context variable in the html/template

class ContactView(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, "contact.html", context)

	# def post(self, request, *args, **kwargs):
	# 	return

	# def put(self, request, *args, **kwargs):
	# 	return




