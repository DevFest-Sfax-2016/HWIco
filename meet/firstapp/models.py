from django.db import models

class Post(models.Model):
    SEXE = (
        ('H', 'Homme'),
        ('F', 'Famme'),
    )
    sexe=models.CharField(max_length=1, choices=SEXE)
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    searchFor =  models.CharField(max_length=1, choices=SEXE)
    mail = models.EmailField()
    pays=models.CharField(max_length=40)
    birthday = models.DateField()

    def __str__(self):
        return self.nom

