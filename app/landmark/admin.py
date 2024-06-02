from django.contrib import admin

from .models import (
    Landmark,
    Location,
    OpeningHour,
    PhotoLandmark,
    TicketPrice,
    UniqueActivity,
)

# Register your models here.
admin.site.register(Landmark)
admin.site.register(Location)
admin.site.register(OpeningHour)
admin.site.register(PhotoLandmark)
admin.site.register(TicketPrice)
admin.site.register(UniqueActivity)
