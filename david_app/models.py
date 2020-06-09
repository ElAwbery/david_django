from django.db import models

# Create a model, inheriting from the Django models class (always make your ORM this way)
class David_app(models.Model):
    # There are many, many fields available, see Django documentation for other types
    # Charfield limits the length, good field to use for titles 
    Name = models.CharField(max_length=20)
    ID = models.IntegerField()
    Role = models.CharField(max_length=20)
    Note = models.TextField()
    Image = models.TextField()

