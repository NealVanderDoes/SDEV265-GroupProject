from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView

from .forms import PostForm, CommentForm, IngredientToRecipeFormSet, IngredientToRecipe, RecipeImgForm
from .models import Post, Comment, RecipeImg


def post_list(request):
    """
    Displays all published posts
    :param request:
    :return:
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """
    Displays a single post with its picture, comments, and ingredients.
    :param request:
    :param pk:
    :return:
    """
    post = get_object_or_404(Post, pk=pk)
    ingredients = IngredientToRecipe.objects.filter(post=post)
    try:
        image = RecipeImg.objects.all()
        return render(request, 'blog/post_detail.html', {'post': post, 'ingredients': ingredients, 'img': image})
    except ValueError:
        return render(request, 'blog/post_detail.html', {'post': post, 'ingredients': ingredients, })


@login_required()
def post_new(request):
    """
    Function for creating a new post. Accesses the various forms and displays them on the page.
    :param request:
    :return:
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        formset = IngredientToRecipeFormSet(request.POST, request.FILES)
        img_form = RecipeImgForm(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid() and img_form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            formset.instance = post
            formset.save()
            img = img_form.save(commit=False)
            img.post = post
            img_form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        formset = IngredientToRecipeFormSet()
        img_form = RecipeImgForm()

    return render(request, 'blog/post_edit.html', {
        'form': form,
        'formset': formset,
        'img_form': img_form
    })


@login_required()
def post_edit(request, pk):
    """
    Function for editing existing posts. Accesses the forms of a post and displays them on the page for editing.
    Allows for deletion of an image.
    :param request:
    :param pk:
    :return:
    """
    post = get_object_or_404(Post, pk=pk)
    recipe_img_instance = RecipeImg.objects.filter(post=post).first()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        formset = IngredientToRecipeFormSet(request.POST, instance=post)
        img_form = RecipeImgForm(request.POST, request.FILES, instance=post)
        if form.is_valid() and formset.is_valid() and img_form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            formset.instance = post
            formset.save()

            if 'img-clear' in request.POST and recipe_img_instance:
                recipe_img_instance.img.delete(save=False)
                recipe_img_instance.delete()

            elif img_form.cleaned_data.get('img'):
                img = img_form.save(commit=False)
                img.post = post
                img.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        formset = IngredientToRecipeFormSet(instance=post)
        img_form = RecipeImgForm(instance=recipe_img_instance)

    return render(request, 'blog/post_edit.html', {
        'form': form,
        'formset': formset,
        'img_form': img_form,
    })


@login_required()
def post_draft_list(request):
    """
    Function for displaying an accounts unpublished draft posts.
    :param request:
    :return:
    """
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required()
def post_publish(request, pk):
    """
    Function for publishing a post.
    :param request:
    :param pk:
    :return:
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.publish()
    return redirect('post_detail', pk=pk)


@login_required()
def post_remove(request, pk):
    """
    Function for removing an accounts post.
    :param request:
    :param pk:
    :return:
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
    return redirect('post_list')


@login_required
def add_comment_to_post(request, pk):
    """
    Function for adding a comment to a post. Accesses the comment form and displays it on the page.
    :param request:
    :param pk:
    :return:
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@staff_member_required()
def comment_approve(request, pk):
    """
    Function for approving a comment. (Admin use only)
    :param request:
    :param pk:
    :return:
    """
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@staff_member_required()
def comment_remove(request, pk):
    """
    Function for removing a comment. (Admin use only)
    :param request:
    :param pk:
    :return:
    """
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


class SignUpView(CreateView):
    """
    Class for creating a new user account. Accesses the user creation form and displays it on the page.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def search_post(request):
    """
    Function for searching for posts. Displays a list of posts that match the search query.
    :param request:
    :return:
    """
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = Post.objects.filter(title__contains=search_query)
        return render(request, 'blog/search_post.html', {'query': search_query, 'posts': posts})
    else:
        return render(request, 'blog/search_post.html', {})
