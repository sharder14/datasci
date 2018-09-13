from django.db import models

# Create your models here.

class Dataset(models.Model):
    dataset = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.dataset

class DataLine(models.Model):
    id = models.AutoField(primary_key=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField(blank = True, null=True)
    cat1 = models.CharField(max_length=200, blank=True)
    cat2 = models.CharField(max_length=200, blank=True) 
    cat3 = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.dataset}  line {self.id}'