from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Place(models.Model):
    sector = models.IntegerField()
    row = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'sector:{self.sector}, row:{self.row}, number:{self.numder}'
    
    class Meta:
        unique_together = (('sector', 'row', 'number'),)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return f'user:{self.user}, place:{self.place}, date:{self.date}'