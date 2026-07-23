from django.db import models

# Create your models here.

import uuid
from django.urls import reverse

class Book(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    title=models.CharField(max_length=100)
    description=models.TextField()
    release_date=models.DateField()
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse("book-details", kwargs={"pk":self.id})