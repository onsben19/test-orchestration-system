from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add other fields as needed

    def __str__(self):
        return self.nom
