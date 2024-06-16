import random

from rest_framework import serializers

from .models import Landmark, Location, LandmarkContent, Language


class LandmarkListSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Landmark
        fields = ("id", "name", "photo")

    def get_photo(self, obj):
        photos = obj.photos.all()
        if photos:
            return random.choice(photos).photo_url
        return None


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("address", "location_url")


class LandmarkDetailSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    photos = serializers.SerializerMethodField()
    unique_activities = serializers.SerializerMethodField()
    opening_hours = serializers.SerializerMethodField()
    ticket_prices = serializers.SerializerMethodField()
    contact_info = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    history = serializers.SerializerMethodField()

    class Meta:
        model = Landmark
        fields = (
            "id",
            "name",
            "description",
            "history",
            "location",
            "photos",
            "unique_activities",
            "opening_hours",
            "ticket_prices",
            "contact_info",
        )

    def get_photos(self, obj):
        return [photo.photo_url for photo in obj.photos.all()]

    def get_unique_activities(self, obj):
        return [activity.name for activity in obj.unique_activities.all()]

    def get_opening_hours(self, obj):
        opening_hours_dict = {}
        for opening_hour in obj.opening_hours.all():
            opening_hours_dict[
                opening_hour.day
            ] = f"{opening_hour.open_time} - {opening_hour.close_time}"
        return opening_hours_dict

    def get_ticket_prices(self, obj):
        ticket_prices_dict = {}
        for ticket_price in obj.ticket_prices.all():
            ticket_prices_dict[ticket_price.age] = ticket_price.price
        return ticket_prices_dict

    def get_contact_info(self, obj):
        return {"phone": obj.phone, "email": obj.email, "website": obj.website}
    
    def get_description(self, obj):
        request = self.context["request"]
        accept_language_header = request.headers.get('Accept-Language')

        user_language = 'English'
    
        if accept_language_header:
            user_language = accept_language_header

        try:
            language = Language.objects.get(name=user_language)
        except Language.DoesNotExist:
            language = Language.objects.get(id=1)

        try:
            landmark_content = LandmarkContent.objects.get(landmark=obj, language=language)
            return landmark_content.description
        except LandmarkContent.DoesNotExist:
            return None

    def get_history(self, obj):
        request = self.context["request"]
        accept_language_header = request.headers.get('Accept-Language')

        user_language = 'English'

        if accept_language_header:
            user_language = accept_language_header            
            
        try:
            language = Language.objects.get(name=user_language)
        except Language.DoesNotExist:
            language = Language.objects.get(id=1)
            
        try:
            landmark_content = LandmarkContent.objects.get(landmark=obj, language=language)
            return landmark_content.history
        except LandmarkContent.DoesNotExist:
            return None
        except Language.DoesNotExist:
            return None
