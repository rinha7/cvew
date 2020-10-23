from django.shortcuts import render

# Create your views here.


# view 정의
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# create view를 작성할 필요가 잇음.
def create(request):
    if request.method == 'POST':
        pass
