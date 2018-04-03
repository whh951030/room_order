from django.contrib import admin

# Register your models here.
from app01.models import *
admin.site.register(MeetingRoom)
admin.site.register(ReserveRecord)
admin.site.register(UserInfo)
