from django.db import models


class Dht11(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mesure #{self.id} : {self.temperature}°C - {self.humidity}% ({self.date.strftime('%d/%m/%Y %H:%M')})"


class Operateur(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom complet")
    adresse = models.CharField(max_length=255, verbose_name="Adresse")
    tel = models.CharField(max_length=30, verbose_name="Téléphone")

    def __str__(self):
        return f"{self.nom} ({self.tel})"

    class Meta:
        verbose_name = "Opérateur"
        verbose_name_plural = "Opérateurs"


class Incident(models.Model):
    STATUS_CHOICES = [
        ('Ouvert', 'Ouvert'),
        ('En cours', 'En cours'),
        ('Résolu', 'Résolu'),
    ]

    date = models.DateTimeField(auto_now_add=True, verbose_name="Date & Heure")
    temperature = models.FloatField(null=True, blank=True, verbose_name="Température relevée (°C)")
    description = models.TextField(verbose_name="Description de l'incident")
    operateur = models.ForeignKey(
        Operateur,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="incidents",
        verbose_name="Opérateur assigné"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Ouvert', verbose_name="Statut")
    dht = models.ForeignKey(
        Dht11,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="incidents",
        verbose_name="Mesure associée"
    )

    def __str__(self):
        return f"Incident #{self.id} - {self.status} ({self.date.strftime('%d/%m/%Y %H:%M')})"

    class Meta:
        verbose_name = "Incident"
        verbose_name_plural = "Incidents"
