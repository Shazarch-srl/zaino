from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    weight = models.FloatField(help_text="Weight in kilograms")
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

