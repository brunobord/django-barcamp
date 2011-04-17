import datetime
from django.test import TestCase
from barcamp.models import Room, Session
from barcamp.helpers import generate_day, generate_day_room

class GeneratorTest(TestCase):

    def setUp(self):
        # create a couple of rooms
        self.room1 = Room.objects.create(name='room1')
        self.room2 = Room.objects.create(name='room2')
        self.today = datetime.date.today()

    def test_generate_room(self):
        generate_day_room(self.room1, self.today,
            start_time=datetime.time(9,0),
            end_time=datetime.time(12,0),
            duration=25,
            pause=5
        )
        self.assertEquals(Session.objects.count(), 6)

    def test_generate_day(self):
        generate_day(self.today,
            start_time=datetime.time(9,0),
            end_time=datetime.time(12,0),
            duration=25,
            pause=5
        )
        self.assertEquals(Session.objects.count(), 12)
