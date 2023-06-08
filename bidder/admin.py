from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Auction)
# admin.site.register(Bids)
admin.site.register(Company)
admin.site.register(Placement)
admin.site.register(Bid)
admin.site.register(PlacementBid)
