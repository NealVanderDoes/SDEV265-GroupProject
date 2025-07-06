from django import forms
from django.forms import inlineformset_factory
from .models import Post, Comment, IngredientToRecipe, RecipeImg


class PostForm(forms.ModelForm):
    """
    PostForm class to make the form blueprint when creating a new blog post.
    """
    class Meta:
        model = Post
        fields = ('author', 'title', 'description')

class RecipeImgForm(forms.ModelForm):
    """
    RecipeImgForm class handles the image upload for a recipe.
    """
    class Meta:
        model = RecipeImg
        fields = ('img',)

# FormSet for managing multiple ingredients linked through IngredientToRecipe
IngredientToRecipeFormSet = inlineformset_factory(
    Post,  # Parent model
    IngredientToRecipe,  # Child model
    fields=('ingredient', 'quantity', 'unit', 'instructions'),
    extra=5,
    can_delete=True,
)




class CommentForm(forms.ModelForm):
    """
    CommentForm class makes the comment blueprint when creating a new comment.
    """
    class Meta:
        model = Comment
        fields = ('author', 'text',)
