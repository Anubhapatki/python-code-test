from django.db import models


class Starship(models.Model):
    name = models.CharField(max_length = 255)
    model = models.CharField(max_length=255)
    starship_class = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    cost_in_credits = models.CharField(max_length=255)
    length = models.FloatField()
    hyperdrive_rating = models.FloatField()
    cargo_capacity = models.BigIntegerField()
    crew = models.IntegerField()
    passengers = models.IntegerField()
    max_atmosphering_speed = models.CharField(max_length=255)
    mglt = models.FloatField()



class Listing(models.Model):
    name = models.CharField(max_length=255)
    ship_type = models.ForeignKey(Starship, related_name='listings')
    price = models.IntegerField()
    active = models.BooleanField(default=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

