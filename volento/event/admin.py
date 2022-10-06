from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(EventCategory)
admin.site.register(EventSponser)
admin.site.register(Event)
admin.site.register(EventImage)
admin.site.register(EventAgenda)
admin.site.register(EventJobCategoryLinking)
admin.site.register(EventMember)
admin.site.register(EventUserWishList)
admin.site.register(UserCoin)



