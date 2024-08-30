from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index_func(request):
    return render(request, 'second_task/func_template.html')


class index_class(TemplateView):
    template_name = 'second_task/class_template.html'
