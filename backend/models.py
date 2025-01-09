from django.db import models

# Create your models here.
class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    photo= models.ImageField(upload_to='Categorie',null=False)
    nom = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.nom



class Plat(models.Model):
    id = models.AutoField(primary_key=True)
    image= models.ImageField(upload_to='Plat',null=False)
    noms = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    prix = models.IntegerField(default=1)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,related_name='Categorie',default=1)

    def __str__(self):
        return self.noms
