from django.db import models

class Inventory(models.Model):
    
    # store the number of chickens
    chickens = models.PositiveIntegerField(default=0)  

    # These are properties of number of chickens
    @property
    def legs(self):
        return self.chickens * 2  #  chicken has 2 legs

    @property
    def wings(self):
        return self.chickens * 2  # here each chicken has 2 wings

    @property
    def flesh(self):
        return self.chickens * 1  # Each chicken has 1 flesh portion (1 kg)

    def __str__(self):
        return f"Inventory: {self.chickens} Chickens (Legs: {self.legs}, Wings: {self.wings}, Flesh: {self.flesh} kg)"
