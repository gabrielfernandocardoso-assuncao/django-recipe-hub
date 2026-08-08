from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes' : recipes
    }

    return render(request, 'recipes/index.html', context)

@login_required()
def new_recipe(request):
    form = RecipeForm(request.POST, request.FILES)

    if request.method != 'POST':
        form = RecipeForm()
    else:
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            new_recipe = form.save(commit=False)

            new_recipe.owner = request.user
            new_recipe.save()

            return HttpResponseRedirect(reverse('index'))

    context = {'form':form}

    return render(request, 'recipes/new_recipe.html', context)