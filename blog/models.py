from django.db import models

class Skuter(models.Model):
    nom = models.CharField("Nomi", max_length=200)
    model = models.CharField("Modeli", max_length=100, blank=True)
    narx_soat = models.DecimalField("kunlik narx (UZS)", max_digits=10, decimal_places=2)
    mavjud = models.BooleanField("Mavjud", default=True)
    rasm = models.ImageField(upload_to='skuter_rasmlari/', blank=True, null=True)
    tavsif = models.TextField("Tavsif", blank=True)
    yaratilgan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} — {self.model or '—'}"
