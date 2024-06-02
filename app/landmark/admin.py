from django.contrib import admin

from .models import (
    Landmark,
    Location,
    OpeningHour,
    PhotoLandmark,
    TicketPrice,
    UniqueActivity,
)


# Custom admin class for Landmark
class LandmarkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "history",
        "phone",
        "email",
        "website",
        "location",
    )


# Register your models here.
admin.site.register(Landmark, LandmarkAdmin)
admin.site.register(Location)
admin.site.register(OpeningHour)
admin.site.register(PhotoLandmark)
admin.site.register(TicketPrice)
admin.site.register(UniqueActivity)
