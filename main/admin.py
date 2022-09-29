from django.contrib import admin

from .models import MessMenu,Hostel,College,FeePaid,FeeRecords

admin.site.register(MessMenu)
admin.site.register(Hostel)
admin.site.register(College)
admin.site.register(FeePaid)
admin.site.register(FeeRecords)