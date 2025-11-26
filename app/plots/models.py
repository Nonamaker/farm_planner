from django.db import models

class Bed(models.Model):
    """ Each bed represents a distinct, continuous plantable area."""
    name = models.TextField()
    # The date the record was added to the system
    date_added = models.DateField(auto_now_add=True)
    # The date the bed was physically established
    date_created = models.DateField(null=True)

    # Dimensional attributes
    # Assuming a simple rectangular bed
    width = models.PositiveSmallIntegerField()  # inches
    length = models.PositiveSmallIntegerField()  # inches


class Plant(models.Model):
    """ Each record represents a unique plant in a specific bed. """
    bed = models.ForeignKey("plots.Bed", on_delete=models.CASCADE)
    name = models.TextField()

    # Assuming all plant footprints are circular
    size = models.PositiveSmallIntegerField()  # The diameter of the mature plant's footprint, inches.
    # Y increases from the top to bottom of a bed
    # X increases from left to right in a bed.
    # The point at which the plant is positioned in the bed.
    position_x = models.PositiveSmallIntegerField()
    position_y = models.PositiveSmallIntegerField()
