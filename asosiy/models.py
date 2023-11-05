from django.db import models

class Club(models.Model):
    nom = models.CharField(max_length=30)
    logo = models.FileField()
    davlat = models.CharField(max_length=30)
    president = models.CharField(max_length=30, blank=True)
    coach = models.CharField(max_length=30, blank=True)
    yili = models.DateField(blank=True)
    record_transfer = models.CharField(max_length=30, blank=True)
    record_sotuv = models.CharField(max_length=30, blank=True)

    def __str__(self):
         return self.nom

class Player(models.Model):
    ism = models.CharField(max_length=30)
    davlat = models.CharField(max_length=30)
    pozitsiya = models.CharField(max_length=30)
    narx = models.PositiveSmallIntegerField()
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    tugilgan_yil = models.DateField()
    def __str__(self):
        return self.ism

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    eski = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="sotuvlari")
    yangi = models.ForeignKey(Club, on_delete=models.CASCADE)
    mavsum = models.CharField(max_length=10)
    narx = models.PositiveSmallIntegerField()
    tah_narx = models.PositiveSmallIntegerField()

class HMavsum(models.Model):
    hovirgi_mavsum = models.CharField(max_length=10)
    def __str__(self):
        return self.hovirgi_mavsum
    class Meta:
        verbose_name = "Hozirgi Mavsum"
        verbose_name_plural = "Hozirgi Mavsum"