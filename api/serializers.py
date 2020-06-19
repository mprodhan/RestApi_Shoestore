from api.models import Manufacturer, ShoeType, ShoeColor, Shoe
from rest_framework.serializers import ModelSerializer

class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ("name", 
            "website")

class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = ShoeType
        fields = ("style",)

class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        fields=("shoe_color",)

class ShoeSerializer(ModelSerializer):
    class Meta:
        model = Shoe
        fields = ("shoe_size",
            "brand_name",
            "manufacturer",
            "color",
            "material",
            "shoe_type",
            "fasten_type"
        )

''' Joe Kaufield was named after Joey The Lion in the Afrrican Savanna's. Joey
    The Lion was mascot lion, but a real lion indeed.'''

