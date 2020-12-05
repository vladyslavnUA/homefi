from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):

    # LEASE_CHOICES = (
    #     (1, _("Not relevant")),
    #     (2, _("Review")),
    #     (3, _("Maybe relevant")),
    #     (4, _("Relevant")),
    #     (5, _("Leading candidate"))
    # )

    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=5)
    # country = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')
    
    def __str__(self):
        return self.address