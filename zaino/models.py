from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField(help_text="Weight in kilograms")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")

    def __str__(self) -> str:
        return self.name

