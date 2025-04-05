from django.db import models

class NumberPair(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    result = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.number1}, {self.number2} -> {self.result}"
