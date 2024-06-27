from django.db import models



class Klass(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Mehmonxona(models.Model):
    name = models.CharField(max_length=100)
    darajasi = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Travel(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    muddati = models.CharField(max_length=100)
    price = models.IntegerField()
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='travel')
    mehmonxona = models.ForeignKey(Mehmonxona, on_delete=models.CASCADE, related_name='travel')

    def __str__(self):
        return self.name