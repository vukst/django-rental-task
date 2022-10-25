from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    previous_reservation = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.rental.name} from {self.start_date} to {self.end_date}"
