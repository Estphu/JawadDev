from django.shortcuts import redirect, render
from .backends import get_random_cake_instance, logs
from .models import Recipe

# Create your views here.
def bake_picker_index(request):

    if request.method=="POST":
        return redirect('bakepicker:cake_and_recipe')

    return render(request, 'bakepicker/bakepicker_index.html')

def cake_and_recipe(request):
    random_cake_instance, result, max_num, logs = get_random_cake_instance()
    related_recipe_instance = Recipe.objects.filter(cake=random_cake_instance)

    context = {
        'cake': random_cake_instance,
        'recipe': related_recipe_instance,
        'results': result,
        'max_num': max_num,
        'logs': logs
    }
    return render(request, 'bakepicker/cake_and_recipe.html', context=context)