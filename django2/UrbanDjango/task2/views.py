from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func_templates(request):
    return render(request, "second_task/func_template.html")