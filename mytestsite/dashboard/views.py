from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    context = {
        "block_title":"Dashborad",
        'news_list': Post.objects.all(),

    }
    return render(request, 'dashborad/index.html', context=context)