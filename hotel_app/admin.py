from django.contrib import admin
from .models import Guest, Hotel, Room, Booking

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    pass

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass

# Register your models here.
