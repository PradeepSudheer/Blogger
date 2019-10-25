from django.shortcuts import render, get_object_or_404
from .models import Blogpost
from Matches.models import matches
# Create your views here.
def home(request):
    blogpost = Blogpost.objects
    matche = matches.objects
    print("12345678")
    return render(request,'Blog/home.html',{'blogposts':blogpost,'matches':matche,})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blogpost,pk = blog_id)
    return render(request,'Blog/detail.html',{'blog':blog_detail})
