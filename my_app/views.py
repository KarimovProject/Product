# Create your views here.
from unicodedata import name
from .models import Product
from django.http import JsonResponse
from django.http import HttpResponse


def home(request):
    return JsonResponse({"k":'v'})

def add(request):
    dict_post = request.POST
    db=Product(
    name =dict_post.get('name'),
    company = dict_post.get('company'),
    color = dict_post.get('color'),
    RAM = dict_post.get('RAM'),
    memory = dict_post.get('memory'),
    price = dict_post.get('price'),
    img_url = dict_post.get('img_url')
    )
    db.save()
    return JsonResponse({})

# def f():
#     url = 'http://127.0.0.1:8000/'
#     r = requests.post(url, params={'name':'s10'})


    