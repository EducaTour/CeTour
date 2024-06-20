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


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "address",
        "location_url",
        "landmark",
    )


class OpeningHourAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "open_time",
        "close_time",
        "landmark",
    )


class PhotoLandmarkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "photo_url",
        "landmark",
    )


class UniqueActivityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "landmark",
    )


class TicketPriceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "age",
        "price",
        "landmark",
    )


# Register your models here.
admin.site.register(Landmark, LandmarkAdmin)
admin.site.register(Language)
admin.site.register(LandmarkContent, LandmarkContentAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(OpeningHour, OpeningHourAdmin)
admin.site.register(PhotoLandmark, PhotoLandmarkAdmin)
admin.site.register(TicketPrice, TicketPriceAdmin)
admin.site.register(UniqueActivity, UniqueActivityAdmin)
