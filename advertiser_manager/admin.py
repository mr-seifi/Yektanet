from django.contrib import admin
from .models import Advertiser, Ad, View, Click


class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ('name', 'reg_date')


class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date')
    list_filter = ('approve', 'pub_date')
    search_fields = ('title',)


class ViewAdmin(admin.ModelAdmin):
    list_display = ('ad', 'viewed_time', 'user_ip')


class ClickAdmin(admin.ModelAdmin):
    list_display = ('view', 'clicked_time', 'user_ip')


admin.site.register(Advertiser, AdvertiserAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(View, ViewAdmin)
admin.site.register(Click, ClickAdmin)
