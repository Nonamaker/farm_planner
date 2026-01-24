""" Contains base models for 'Stock' defined as any object, physical or digital, kept in a trackable state, i.e.
inventory or livestock. """
import uuid
from django.db import models
 
 
class Stock(models.Model):
    """ Any object, physical or otherwise, to be tracked in some way. """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    @property
    def summary(self):
        """ Returns a very brief summary of what the stock consists of. """
        elements = []
        if self.livestock_data is not None:
            elements.append('Livestock')
            elements.append(self.livestock_data.summary)
        return ' | '.join(elements)

class LiveStock(models.Model):
    """ Any animal stock to be tracked. """
    stock = models.OneToOneField('stock.Stock', related_name='livestock_data', on_delete=models.deletion.CASCADE)
    dob = models.DateField()  # Date of birth
    dod = models.DateField(blank=True, null=True)  # Date of death
    sex = models.TextField()

    # property age

    @property
    def summary(self):
        """ Returns a very brief summary of what the livestock is. """
        elements = []
        elements.append(self.sex)
        #elements.append(self.age)
        if self.chicken_data is not None:
            elements.append("Chicken")
            elements.append(self.chicken_data.summary)
        return ' | '.join(elements)


class Breed(models.Model):
    """ Encapsulates data for a specific breed of Chicken. """
    name = models.TextField()
    mature_age = models.PositiveSmallIntegerField()   # In weeks. This is not necessarily the date they are fully grown, just sexually mature.

    def __str__(self):
        return self.name


class Chicken(models.Model):
    """ Encapsulates data and logic specific to chickens. """
    # Note: Only solving for the current needs. Not bothering with abstractions such as 'poultry' etc. for the time being.
    #  Solving the specific case and will abstract as needed at a later date.
    livestock = models.OneToOneField('stock.LiveStock', related_name='chicken_data', on_delete=models.deletion.CASCADE)
    breed = models.ForeignKey('stock.Breed', on_delete=models.deletion.RESTRICT)
    band_color = models.TextField()
    band_number = models.PositiveSmallIntegerField(null=True)

    @property
    def summary(self):
        """ Returns a very brief summary of what the livestock is. """
        elements = []
        elements.append(self.breed)
        return ' | '.join(elements)


class Hatch(models.Model):
    """ Records the conditions during incubation and up until the last chick from the brood has hatched.
        Known limitations:
        - Only handles single-breed broods.
        - The 'create_chickens' does not distinguish between early/late hatching chickens. DOB is the final date for all records.
        - No support for non-chicken birds.
        - No support for incubation conditions (temp/rotation frequency/etc.)
    """
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    equipment = models.TextField()
    notes = models.TextField()
    eggs_started = models.PositiveSmallIntegerField()
    eggs_hatched = models.PositiveSmallIntegerField(null=True)
    first_hatch_date = models.DateField(null=True)
    breed = models.ForeignKey('stock.Breed', on_delete=models.deletion.RESTRICT)
    complete = models.BooleanField(default=False)  # Flag whether the event is finalized

    @property
    def survival_rate(self):
        """ Returns the rate of succesful hatch. """
        return self.eggs_hatched / self.eggs_started
    
    def create_chickens(self):
        """ Creates a number of Chicken records depending on the data from the Hatch. """
        for _ in range(self.eggs_hatched):
            stock = Stock.objects.create()
            livestock = LiveStock()
            livestock.stock = stock
            livestock.dob = self.end_date
            livestock.save()
            Chicken.objects.create(
                livestock=livestock,
                breed=self.breed
            )
            

class Egg(models.Model):
    stock = models.OneToOneField('stock.Stock', related_name='egg_data', on_delete=models.deletion.CASCADE)
    lay_date = models.DateField()
    condition = models.TextField()  # i.e. dirty, cracked, small


class MRO(models.Model):
    """ Maintenance, Repair, and Operating stock. """
    stock = models.OneToOneField('stock.Stock', related_name="MRO_data", on_delete=models.deletion.CASCADE)


class FinishedGoods(models.Model):
    """ Represents finished goods ready for sale. """
    stock = models.OneToOneField('stock.Stock', related_name="finished_goods_data", on_delete=models.deletion.CASCADE)
    name = models.TextField() # i.e. '1-doz. carton of eggs'

    # TODO Should probably abstract sales out to its own app.
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_date = models.DateField()


class RawMaterials(models.Model):
    """ Represents raw materials used in the production of Finished Goods. """
    stock = models.OneToOneField('stock.Stock', related_name="raw_material_data", on_delete=models.deletion.CASCADE)


# class Notes(models.Model):
# """ Records a note about a piece of stock. """
#   stock = models.OneToManyField('stock.Stock', related_name='notes', on_delete=models.deletion.CASCADE)
#   note = models.TextField()
#   date = models.DateField(auto_now_add=True)