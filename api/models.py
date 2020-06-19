from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class ShoeType(models.Model):
    style = models.CharField(max_length=30)

    def __str__(self):
        return self.style

class ShoeColor(models.Model):
    RED = 'RD'
    ORANGE = 'OR'
    YELLOW = 'YE'
    GREEN = 'GR'
    BLUE = 'BL'
    INDIGO = 'IN'
    VIOLET = 'VT'
    WHITE = "WH"
    BLACK = "BL"
    SHOE_COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black')
    ]

    shoe_color = models.CharField(
        max_length=2,
        choices=SHOE_COLOR_CHOICES,
        default=RED,
    )

    def __str__(self):
        return self.shoe_color

class Shoe(models.Model):
    shoe_size = models.IntegerField()
    brand_name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=30)