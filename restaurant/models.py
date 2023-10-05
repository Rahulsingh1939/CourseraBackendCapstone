
from django.db import models
from django.core.validators import MinValueValidator
from datetime import date

# Create your models here.
class Booking(models.Model):
    MIN_NO_OF_QUEST = 0

    name = models.CharField(
        max_length = 255,
        null = False,
        help_text = "Booker's name",
    )
    no_of_quest = models.SmallIntegerField(
        validators = [MinValueValidator(MIN_NO_OF_QUEST, f"Number of guest must be greater than {MIN_NO_OF_QUEST}")],
        help_text = "Number of guest",
    )
    booking_date = models.DateField(
        default = date.today,
        help_text = "Booking date",
    )


    def __str__(self):
        return f'{self.name}({self.booking_date})'


# Add code to create Menu model
class Menu(models.Model):
    title = models.CharField(
        max_length=255,
        unique = True,
        help_text='Title',
        db_index=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Price',
        db_index=True,
    )
    inventory = models.SmallIntegerField(
        help_text = "Inventory",
    )

    def __str__(self):
          return f'{self.title}[{self.price}]'