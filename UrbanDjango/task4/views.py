from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def platform(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'fourth_task/platform.html', context)

def games(request):
    title = "Магазин компьютерных игр"
    context = {
        'title': title,
        'games': ['Atomic Heard', 'Cyberpunk 2077', 'PayDay 2'],
    }
    return render(request, 'fourth_task/games.html', context)



class cart(TemplateView):
    title = 'Корзина'
    text = 'Извините, Ваша корзина пуста'
    context = {
        'title': title,
        'text': text,
    }
    template_name = 'fourth_task/cart.html'

    def get_context_data(self, **kwargs):
        return self.context

