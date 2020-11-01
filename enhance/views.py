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
        post.save()

        return render(request, 'enhance/enhance_main.html',{'url':"/media/images/raw/"+str(img)})
    else:
        return render(request, 'enhance/enhance_main.html')

def detail(request):
    if request.method == "POST":
        img = request.POST['img_name']
        print(img)
    return render(request, 'enhance/enhance_detail.html',{'url_before':img})