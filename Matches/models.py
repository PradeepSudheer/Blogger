from django.db import models

# Create your models here.
class matches(models.Model):
    home_team = models.CharField(max_length=50,null=False)
    away_team = models.CharField(max_length=50,null=False)
    score = models.CharField(max_length=20,null=False)

    def __str__(self):
        return  "{} Vs {}".format(self.home_team,self.away_team)