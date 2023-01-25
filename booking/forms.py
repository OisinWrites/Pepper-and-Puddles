from django import forms
from .models import Booking, Confirmed_Bookings, Table


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'guests', 'date', 'phone', 'email']


class ConfirmedBookingsForm(forms.ModelForm):
    class Meta:
        model = Confirmed_Bookings
        fields = ['table', 'start_time', 'end_time']


class AddTable(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['table_id', 'capacity']
