import re
from django.contrib import admin
from allsellapp.models import HomeBanner, BannerImgs




class BannerImageAdmin(admin.StackedInline):
    model = BannerImgs


@admin.register(HomeBanner)
class BannerAdmin(admin.ModelAdmin):
    inlines = [BannerImageAdmin]
    
    class Meta:
        model = HomeBanner