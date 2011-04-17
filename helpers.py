import datetime
from barcamp.models import Session, Room

def generate_day_room(room, day, start_time, end_time, duration, pause):
    "Generate a schedule for a room"
    start = datetime.datetime(day.year, day.month, day.day, start_time.hour, start_time.minute)
    true_end_time = datetime.datetime(day.year, day.month, day.day, end_time.hour, end_time.minute)
    while start < true_end_time:
        end = start + datetime.timedelta(minutes=duration + pause)
        Session.objects.create(room=room, start_time=start, end_time=end)
        start = end


def generate_day(day, start_time, end_time, duration, pause):
    "Generate a schedule for a day."
    for room in Room.objects.all():
        generate_day_room(room, day, start_time, end_time, duration, pause)
        
