from django.db import models



class Transaction(models.Model):
    """ Each record represents an expense or sale. """
    value = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField()
    category = models.TextField()


#class TransactionItem(model.Model):
#    """ Each record links a specific stock item to a Transaction. """


#class Receipt(models.Model):
    # link image file to Transaction record 1:M