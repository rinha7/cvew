from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post

def index(request):
    return HttpResponse("Django main page")

def create(request):
    if request.method == "POST":
        img = request.FILES.get('imgs')
        post = Post()
        post.photo = img
        print("image's name is = ",str(img))
        post.save()

        return render(request, 'enhance/enhance_main.html',{'url':"/media/images/raw/"+str(img)})
    else:
        return render(request, 'enhance/enhance_main.html')

def detail(request):
    return HttpResponse("THIS IS DETAIL PAGE")