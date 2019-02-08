from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return '%s %s %s' % (self.id, self.name, self.email)

    class Meta:
        app_label = 'homePage'
        verbose_name = 'Subscriber'
