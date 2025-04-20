from django.db import models

class Car(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plate_number = models.CharField(max_length=10, primary_key=True, unique=True)
    brand = models.CharField(max_length=50, editable=True)
    model = models.CharField(max_length=100, editable=True)
    year = models.IntegerField(editable=True)
    price = models.FloatField(editable=True)
    loan = models.FloatField(editable=True, null=True, blank=True)
    interest = models.IntegerField(editable=True, null=True, blank=True)
    

    class Meta:
        ordering = ['brand', '-model']
        verbose_name_plural = 'Cars'
    
    def __str__(self):
        return f'{self.plate_number} - {self.brand} {self.model}'

class Service(models.Model):
    car = models.ForeignKey(
        "Car",
        to_field='plate_number',
        on_delete=models.CASCADE,
    )
    date = models.DateField(editable=True)
    description = models.TextField(editable=True)
    cost = models.FloatField(editable=True)

    class Meta:
        ordering = ['car', '-date']
        verbose_name_plural = 'Services'