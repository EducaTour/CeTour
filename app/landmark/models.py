from django.db import models


class Location(models.Model):
    address = models.CharField(max_length=255)
    location_url = models.URLField()

    def __str__(self):
        return self.address


class Landmark(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    history = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()
    location = models.OneToOneField(
        Location, on_delete=models.CASCADE, related_name="landmark"
    )

    def __str__(self):
        return self.name


class PhotoLandmark(models.Model):
    photo_url = models.URLField()
    landmark = models.ForeignKey(
        Landmark, on_delete=models.CASCADE, related_name="photos"
    )

    def __str__(self):
        return self.photo_url


class UniqueActivity(models.Model):
    name = models.CharField(max_length=255)
    landmark = models.ForeignKey(
        Landmark, on_delete=models.CASCADE, related_name="unique_activities"
    )

    def __str__(self):
        return self.name


class OpeningHour(models.Model):
    day = models.CharField(max_length=10)
    open_time = models.TimeField()
    close_time = models.TimeField()
    landmark = models.ForeignKey(
        Landmark, on_delete=models.CASCADE, related_name="opening_hours"
    )

    def __str__(self):
        return f"{self.day}: {self.open_time} - {self.close_time}"


class TicketPrice(models.Model):
    age = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    landmark = models.ForeignKey(
        Landmark, on_delete=models.CASCADE, related_name="ticket_prices"
    )

    def __str__(self):
        return f"{self.age}: {self.price}"
