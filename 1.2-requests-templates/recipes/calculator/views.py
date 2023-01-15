from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def menu(request, recipe):
    template_name = 'calculator/index.html'
    num = int(request.GET.get("num", 1))

    context = {
        'recipe': {
            'ингредиент1': 'количество1',
            'ингредиент2': 'количество2',
        },
        'home': {
            'Главная страница': reverse('home')
        },
        'num': num,
    }

    for k, i in DATA[recipe].items():
        DATA[recipe][k] = round(i * num, 2)

    context['recipe'] = DATA[recipe]

    return render(request, template_name, context)


def home_view(request):

    template_name = 'calculator/home.html'
    all_menu = DATA.keys()

    context = {
        'all_menu' : all_menu,

    }
    return render(request, template_name, context)
