from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from django.core import serializers
import simplejson as json
# Create your views here.
def index(request):
    cards = Post.objects.values()
    # print(cards)
    for card in cards:
        
        card["complete_rate"]="{:.0f}".format( (card['production_capacity'] / card['need_production_capacity'])*100 )
        card["good_rate"]="{:.0f}".format((card['good_production'] / card['production_capacity']) * 100)
        ago_time_str = str(timezone.now() - card["fiex_time"]).split(",")[0]
        
        card["fiex_time"] = time2str(ago_time_str.split(":"))
        # print(timezone.now() - card["fiex_time"])
    context = {
        "block_title":"Dashborad",
        'cards': cards,

    }
    return render(request, 'dashborad/dashbord.html', context=context)

def update():
    cards = Post.objects.values()
    # print(cards)
    for card in cards:
        
        card["complete_rate"]="{:.0f}".format( (card['production_capacity'] / card['need_production_capacity'])*100 )
        card["good_rate"]="{:.0f}".format((card['good_production'] / card['production_capacity']) * 100)
        ago_time_str = str(timezone.now() - card["fiex_time"]).split(",")[0]
        
        card["fiex_time"] = time2str(ago_time_str.split(":"))
        # print(card["fiex_time"])
        
    # print(type(cards))
    # tmpJson = serializers.serialize("json",cards)
    # tmpObj = json.loads(tmpJson)
    context = {
        'cards': list(cards),
    }
    
    # tmpObj = json.loads(tmpJson)
    return json.dumps(context,use_decimal=True)


def time2str(time):
    if len(time)==1:
        return time[0]
    else:
        # print(time[1])
        # time_str = ""
        hr = int(time[0])
        if hr > 0:
            return "{} hr".format(hr)
        min = int(time[1])
        if int(time[1]) > 0:
            return "{} min".format(min)
        
        
        return "a few" 
