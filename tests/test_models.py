from django.test import SimpleTestCase, TestCase
from datetime import date
from restaurant.models import Menu, Booking


class MenuTest(TestCase):
    databases = {'default'}
    TestData = {
        'title' : 'Title',
        'price' : 123.45,
        'inventory' : -2,
    }

    def test_check_instance(self):
        item = Menu.objects.create(title = self.TestData['title'],
                                   price = self.TestData['price'],
                                   inventory = self.TestData['inventory'],
                                   )
        self.assertTrue(item.title == self.TestData["title"] and
                        item.price == self.TestData["price"] and
                        item.inventory == self.TestData["inventory"]
                        )


class BookingTest(TestCase):
    databases = {'default'}
    TestData = {
        'name': "Booker's name",
        'no_of_quest': 999,
        'booking_date':  date(year = 2099,
                              month = 6,
                              day = 7
                              ),
    }

    def test_check_instance(self):
        item = Booking.objects.create(name = self.TestData['name'],
                                      no_of_quest = self.TestData['no_of_quest'],
                                      booking_date = self.TestData['booking_date'],
                                      )
        self.assertTrue(item.name == self.TestData["name"] and
                        item.no_of_quest == self.TestData["no_of_quest"] and
                        item.booking_date == self.TestData["booking_date"]
                        )

    def test_check_instance_default(self):
        item = Booking.objects.create(name = self.TestData['name'],
                                      no_of_quest = self.TestData['no_of_quest'],
                                      )
        self.assertTrue(item.name == self.TestData["name"] and
                        item.no_of_quest == self.TestData["no_of_quest"] and
                        item.booking_date == date.today()
                        )
