from django.shortcuts import render,HttpResponse,redirect
import datetime
from functools import wraps
from app01.models import *
import pprint
# Create your views here.
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    name=request.POST.get('name')
    password=request.POST.get('password')
    user_obj=UserInfo.objects.filter(username=name,password=password).first()
    if not user_obj:
        return redirect('/login/')
    else:
        request.session['userid']=user_obj.id
        return redirect('/room/')
def check_login(func):
    @wraps(func)
    def inner(request,*args,**kwargs):
        userid=request.session.get('userid')
        if not userid:
            return redirect('/login/')
        else:
            request.userid=userid
        return func(request,*args,**kwargs)
    return inner
@check_login
def room(request):
    if request.method=='GET':
        select_date=request.GET.get('select_date',None)
        if select_date==None:
            select_date=datetime.datetime.now().date().strftime("%Y-%m-%d")
        print(select_date,type(select_date))
        room_list=MeetingRoom.objects.all().values('id','name')
        time_tuple=ReserveRecord.time1


        new_dic={}
        for dic in room_list:
            new_dic[dic['id']]={
                'id':dic['id'],
                'name':dic['name'],
                'times':{
                    1:False,
                    2:False,
                    3:False,
                    4:False,
                    5:False,
                    6:False,
                    7:False,
                    8:False,
                    9:False,
                    10:False,
                    11:False,
                    12:False,
                    13:False,
                }
            }

        record_list=ReserveRecord.objects.filter(data=select_date).values('room_id','timeline')
        for dic in record_list:
            new_dic[dic['room_id']]['times'][dic['timeline']]=True

        return render(request,'room_list.html',locals())
    else:
        # < QueryDict: {'select_date': ['2018-03-09'], '1': ['1'], '2': ['1', '2'], '3': ['1', '2'],
        # 'csrfmiddlewaretoken': ['PQaYpkXQO8sK7NchY7PC5R09pud0Rwb2ljRfy5uC0VHvurCU70zxn8OnjtBlD7Oj']} >
        data=dict(request.POST)
        userid=request.userid
        select_date=request.POST.get('select_date')
        print(select_date,type(select_date))
        print(data)
        for i,j in data.items():
            if i=='select_date' or i=='csrfmiddlewaretoken':
                continue
            for k in j:
                ReserveRecord.objects.create(data=select_date,user_id=userid,room_id=i,timeline=k)
        return redirect('/room/?select_date=%s' %select_date)




