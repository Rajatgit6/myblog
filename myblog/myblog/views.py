from django.http import HttpResponse
from django.shortcuts import render
from Blog.models import blog
#def home(request):
	#return render(request,"index.html")
def frontpage(request):
	posts=blog.objects.all()

	return render(request,"front.html",{'posts':posts})
def post_details(request,slug):
	post=blog.objects.get(slug=slug)
	return render(request, 'blug_details.html',{'post':post})
