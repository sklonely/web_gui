from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
# Create your views here.
def index(request):
    cards = Post.objects.values()
    # print(cards)
    for card in cards:
        
        card["complete_rate"]="{:.0f}".format( (card['production_capacity'] / card['need_production_capacity'])*100 )
        card["good_rate"]="{:.0f}".format((card['good_production'] / card['production_capacity']) * 100)
        card["fiex_time"] = str(timezone.now() - card["fiex_time"]).split(",")[0]
        # print(timezone.now() - card["fiex_time"])
    context = {
        "block_title":"Dashborad",
        'cards': cards,

    }
    return render(request, 'dashborad/dashbord.html', context=context)