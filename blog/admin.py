from django.contrib import admin

from .models import Post, Comment, IngredientToRecipe


class IngredientToRecipeInline(admin.TabularInline):
    """
    Admin site configuration for IngredientToRecipe model.
    model variable specifies the model to be used.
    extra variable specifies the number of extra rows to be displayed.
    fields variable displays the fields to be displayed in the admin site.
    """
    model = IngredientToRecipe
    extra = 1
    fields = ('ingredient', 'quantity', 'unit', 'instructions')


class PostAdmin(admin.ModelAdmin):
    """
    Admin site configuration for Post model.
    inlines variable displays the inline model to be displayed for post creation.
    """
    inlines = [IngredientToRecipeInline]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
