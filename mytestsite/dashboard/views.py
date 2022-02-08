from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, JyrTable
from django.utils import timezone
from django.core import serializers
from datetime import datetime,timedelta, date
import simplejson as json
from django.db.models import Count
import pandas as pd
import random
from asgiref.sync import sync_to_async


item_conut = 0


# Create your views here.
def index(request):
    result = (JyrTable.objects
    .values('machine_name')
    .annotate(dcount=Count('machine_name'))
    .order_by())
    # machines = []

        
    machines = [{"machine_name":i['machine_name']} for i in result]

    context = {
        'cards': machines,#list(cards)
    }

    return render(request, 'dashborad/dashbord.html',context=context)

@sync_to_async
def get_now():
    global item_conut
    cards = JyrTable.objects.filter(timestamp__gte=date.today()).values()
    now_item_count = len(cards)
    if now_item_count != item_conut and now_item_count!= 0:
        q = pd.DataFrame(cards).sort_values('timestamp')
        item_conut = now_item_count
        return q,item_conut
    else:
        return None,None
    
@sync_to_async
def update():
    data_arrangement()
    cards = Post.objects.values()

    for card in cards:
        
        ago_time_str = str(timezone.now() - card["state_time"]).split(",")[0]
        card["fixtime"] = time2str(ago_time_str.split(":"))

        

    context = {
        'cards': list(cards),#list(cards)
    }
    
    return json.dumps(context,use_decimal=True,default=json_serial)


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


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

@sync_to_async
def data_arrangement():
    try:
        r,idx = get_now() # 模擬更新
        if r is None:
            return
        machine_name_groups =r.groupby(['machine_name'])
        for machine_name,machine_cards in machine_name_groups:
            card_r = machine_cards.sort_values(by = 'timestamp').iloc[-1] #取最新

            try:
                card={
                    "machine_name":card_r['machine_name'],
                    "code":card_r['controller_path_program_runno'],
                    "state":int(card_r['controller_system_status']),
                    "activation":int(0),
                    # "starting_part_count":int(r['controller_part_count'].values[0])
                }
                controller_part_count = int(r['controller_part_count'])
            except :
                return

            # 取得資料庫
            now_state_time = pd.Timestamp(card_r["timestamp"]).to_pydatetime().replace(tzinfo=None)
            now_state = "1" if card['state'] == 11 else "0"
            instance, created = Post.objects.get_or_create(machine_name=card["machine_name"], defaults=card)
        
            if created:
                # 創建初始化
                print('init {}'.format(instance.machine_name))
                instance.state_time = now_state_time
                instance.starting_time = now_state_time
                instance.state_array = now_state
                instance.starting_part_count = controller_part_count
                instance.part_count = controller_part_count - instance.starting_part_count
            elif not created:
                # 第二次之後 判斷有無跨日
                last_state_time = instance.state_time.replace(tzinfo=None)
                time_diff = now_state_time - last_state_time
                # 跨日判斷
                if is_next_day(now_state_time,instance.starting_time):
                    instance.state_time = now_state_time
                    instance.starting_time = now_state_time
                    instance.state_array = now_state
                    instance.starting_part_count = controller_part_count
                    instance.part_count = controller_part_count - instance.starting_part_count
                else:
                    print(card['machine_name'],now_state_time-instance.starting_time.replace(tzinfo=None))
                    last_state = "1" if instance.state == 11 else "0" #上一次的狀態 (資料庫內部的)
                    # 每秒鐘 或 狀態發生變化 更新
                    if last_state != now_state:
                        # 依造時間差新增過往狀態到 時間 t-1 
                        state_temp ="".join(last_state for _ in range(int(time_diff.seconds//60)-1))
                        # 判斷狀態有沒有改變 新增現在狀態到 t 
                        state_temp +=(now_state if last_state!= now_state else last_state)

                        print("    load {}".format(idx),state_temp,int(time_diff.seconds // 60))
                    
                    
                        #更新資料庫
                        instance.state_time = now_state_time #更新時間
                        instance.part_count = controller_part_count - instance.starting_part_count
                        instance.state_array += state_temp
                    # print(int((instance.state_array.count('1') / len(instance.state_array))*100))

                    card['activation'] = int((instance.state_array.count('1') / len(instance.state_array))*100)

                    for attr, value in card.items():
                        setattr(instance, attr, value)
                

        
            instance.save()
    except 1:
        print("err from {}".format(idx))
        pass


def is_next_day(now_state_time,starting_time):
    if (now_state_time.date() - starting_time.replace(tzinfo=None).date()) >= timedelta(days=1):
        print("換日")
        return True
    else:
        return False
