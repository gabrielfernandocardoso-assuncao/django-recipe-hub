from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    # title
    title = models.CharField(max_length=200)
    # ingredients
    ingredients = models.TextField()
    # instructions
    instructions = models.TextField()
    # prep_time
    prep_time = models.IntegerField()
    # owner
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # img
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'recipes'

    def __str__(self):
        return self.title 