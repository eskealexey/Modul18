from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def platform(request):
    return render(request, 'third_task/platform.html')

def games(request):
    title = "Магазин компьютерных игр"
    list_ = ['Atomic Heard', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'title': title,
        'list_': list_,
    }
    return render(request, 'third_task/games.html', context)



class cart(TemplateView):
    title = 'Корзина'
    text = 'Извините, Ваша корзина пуста'
    context = {
        'title': title,
        'text': text,
    }
    template_name = 'third_task/cart.html'

    def get_context_data(self, **kwargs):
        return self.context

