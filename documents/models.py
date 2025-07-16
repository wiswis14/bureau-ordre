from django.db import models

class Document(models.Model):
    TYPE_CHOICES = [
        ('entrant', 'Entrant'),
        ('sortant', 'Sortant'),
    ]

    numero_texte = models.CharField(max_length=50)
    titre = models.CharField(max_length=255)
    secteur = models.CharField(max_length=100)
    date_enregistrement = models.DateField()
    type_document = models.CharField(max_length=10, choices=TYPE_CHOICES)
    fichier = models.FileField(upload_to='documents/')
    commentaire = models.TextField(blank=True)

    def __str__(self):
        return f"{self.numero_texte} – {self.titre}"
