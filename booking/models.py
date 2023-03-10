from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


class Booking(models.Model):
    name = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    email = models.EmailField()
    date = models.DateTimeField()
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(16)],
                                         null=True)
# Make bookings objects list by name variable

    def __str__(self):
        return self.name


class Table(models.Model):
    table_no = models.CharField(max_length=2, blank=False, null=True)
    table_id = models.IntegerField(validators=[MinValueValidator(1),
                                               MaxValueValidator(12)],
                                   null=True, unique=True)
    capacity = models.IntegerField(validators=[MinValueValidator(1),
                                               MaxValueValidator(4)],
                                   null=True)
    available = models.BooleanField(default=True)

# Function to mark open table as booked,
# or return that it is already booked otherwise.

    def reserve(self):
        if self.available:
            self.available = False
            self.save()
            return True
        else:
            return False

    def __str__(self):

        return self.table_no


class Confirmed_Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        table = self.table
        if table.available:
            table.book()
            super().save(*args, **kwargs)
        else:
            bookings = Confirmed_Booking.objects.filter(table=table)
            for booking in bookings:
                if (self.start_time < booking.end_time and
                    self.start_time > booking.start_time) or (
                 self.end_time < booking.end_time and
                 self.end_time > booking.start_time):
                    raise ValueError(
                        "Table is already reserved during this time.")
            table.reserve()
            super().save(*args, **kwargs)

        def __str__(self):
            return self.name
