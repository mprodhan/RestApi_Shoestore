from django.db import models

class FootWear(models.Model):
    manufac_name = models.CharField(max_length=30)

    SNEAKER = 'SN'
    BOOT = 'BT'
    SANDAL = 'SL'
    DRESS = 'DR'
    OTHER = 'OT'
    SHOE_STYLE_CHOICES = [
        (SNEAKER, 'Sneaker'),
        (BOOT, 'Boot'),
        (SANDAL, 'Sandal'),
        (DRESS, 'Dress'),
        (OTHER, 'Other'),
    ]

    shoe_style = models.CharField(
        max_length=10,
        choices=SHOE_STYLE_CHOICES,
        default=SNEAKER,
    )

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

    Shoe_Color = models.CharField(
        max_length=2,
        choices=SHOE_COLOR_CHOICES,
        default=RED,
    )

    def __str__(self):
        return self.manufac_name

class Shoe(models.Model):
    shoe_size = models.IntegerField()
    brand_name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(FootWear, on_delete=models.CASCADE, 
        related_name="+")
    color = models.ForeignKey(FootWear, on_delete=models.CASCADE, 
        related_name="+")
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(FootWear, on_delete=models.CASCADE, 
        related_name="+")
    fasten_type = models.CharField(max_length=30)

    def __str__(self):
        return self.brand_name