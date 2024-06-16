from django.contrib import admin

from .models import (
    Landmark,
    LandmarkContent,
    Language,
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
        "phone",
        "email",
        "website",
        "location",
    )


class LandmarkContentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "history",
        "landmark",
        "language",
    )


# Register your models here.
admin.site.register(Landmark, LandmarkAdmin)
admin.site.register(Language)
admin.site.register(LandmarkContent, LandmarkContentAdmin)
admin.site.register(Location)
admin.site.register(OpeningHour)
admin.site.register(PhotoLandmark)
admin.site.register(TicketPrice)
admin.site.register(UniqueActivity)
