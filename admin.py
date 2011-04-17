from django.contrib import admin
from barcamp.models import Room, Session

class SessionAdmin(admin.ModelAdmin):
    list_display = ('topic_title', 'start_time', 'end_time')
    list_filter = ('room',)

admin.site.register(Room)
admin.site.register(Session, SessionAdmin)
