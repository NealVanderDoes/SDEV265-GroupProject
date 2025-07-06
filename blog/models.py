from django.db import models
from django.utils import timezone


# Create your models here.
class IngredientToRecipe(models.Model):
    """
    IngredientToRecipe model is the format for storing ingredients information in the database.
    post variable specifies the parent model with a ForeignKey.
    ingredient variable allows naming of an ingredient.
    quantity variable allows specifying the quantity of an ingredient.
    unit variable allows specifying the unit of an ingredient.
    instructions variable allows specifying the instructions for preparing an ingredient.
    """
    CUPS = 'Cups'
    TABLESPOON = 'tbsp'
    TEASPOONS = 'tsp'
    OUNCES = 'oz'
    POUNDS = 'lbs'
    GRAMS = 'g'
    MILLILITERS = 'mL'
    FLUID_OUNCES = 'fl oz'

    UNIT_CHOICES = [
        (CUPS, 'Cups'),
        (TABLESPOON, 'Tablespoon'),
        (TEASPOONS, 'Teaspoons'),
        (OUNCES, 'Ounces'),
        (POUNDS, 'Pounds'),
        (GRAMS, 'Grams'),
        (MILLILITERS, 'Milliliters'),
        (FLUID_OUNCES, 'Fluid Ounces'),
    ]

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES, null=True, blank=True)
    instructions = models.CharField(max_length=50, null=True, blank=True)


class RecipeImg(models.Model):
    """
    RecipeImg model is the format for storing images for recipes.
    post variable specifies the parent model with a ForeignKey.
    img variable allows storing an image for a recipe.
    """
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/', null=True, blank=False)


class Post(models.Model):
    """
    Post model is the format for storing blog posts.
    author variable allows naming of the author of a blog post.
    title variable allows naming of the title of a blog post.
    description variable allows specifying the description of a blog post.
    created_date variable automatically sets the date and time when a blog post is created.
    published_date variable automatically sets the published date of a blog post.
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        publish method finds the current date and time and sets it as the published date.
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        """
        Shows approved comments on posts.
        """
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    """
    Comment class is the format for storing comments on blog posts.
    """
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        """
        Checks if the comment is approved and saves it.
        """
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
