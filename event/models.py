from django.db import models

# Create your models here.
class Speakers(models.Model):
    image = models.ImageField(upload_to="speakers/speakers")
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    Speciality = models.CharField(max_length=20)
    create_date = models.DateField(auto_created=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Speakers'
        verbose_name_plural = 'Speakers'

class Schedule(models.Model):
    time = models.TimeField(blank=True, null=True)
    Theme = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True, null=True)

    speakers = models.ForeignKey(Speakers, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.speakers}'

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedule'

class Schedule_day(models.Model):
    day = models.CharField(max_length=20, blank=True, null=True)
    schedule = models.ManyToManyField(Schedule, blank=True, null=True)

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = 'Schedule_Day'
        verbose_name_plural = 'Schedule_Day'

class Hotels(models.Model):
    image = models.ImageField(upload_to="hotels/hotels")
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Hotels'
        verbose_name_plural = 'Hotels'

class Gallery(models.Model):
    images = models.ImageField(upload_to="gallery/gallery")

class Sponsors(models.Model):
    images = models.ImageField(upload_to="sponsors/sponsors")

class TDescription(models.Model):
    description = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'TDescription'
        verbose_name_plural = 'TDescription'

class Tickets(models.Model):
    type = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    description = models.ManyToManyField(TDescription)
    description_m = models.ManyToManyField(TDescription, related_name='mute_t_d')

    def __str__(self):
        return f'{self.type} {self.price}'

    class Meta:
        verbose_name = 'Tickets'
        verbose_name_plural = 'Tickets'