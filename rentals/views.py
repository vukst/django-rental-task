from django.shortcuts import render

from .models import Rental, Reservation


def rentalTable(request):
    rentals = Rental.objects.all()
    reservations = Reservation.objects.all()
    return render(
        request, "rentalTable.html", {"rentals": rentals, "reservations": reservations}
    )
