from django.db import models


class VariationManager(models.Manager):
    def colours(self):
        return super(VariationManager, self).filter(variation_category='colour', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)