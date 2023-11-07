from django.contrib import admin
from django.contrib.auth.models import *
from .models import  *

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ["id","nom", "davlat"]
    list_filter = ["davlat"]
    search_fields = ["nom"]

admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "davlat", "pozitsiya", "club"]
    list_filter = ["club"]
    search_fields = ["ism","club__nom","id"]

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ["id", "player", "eski", "yangi", "mavsum"]
    list_filter = ["mavsum"]
    search_fields = ["player__ism", "eski", "yangi"]


# admin.site.register(Club
# admin.site.register(Player)
# admin.site.register(Transfer)
admin.site.register(HMavsum)
