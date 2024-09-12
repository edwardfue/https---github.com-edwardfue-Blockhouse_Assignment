from django.contrib import admin
from .models import CandleStickchart, Linechart, Barchart, Piechart

admin.site.register(CandleStickchart)
admin.site.register(Linechart)
admin.site.register(Barchart)
admin.site.register(Piechart) 