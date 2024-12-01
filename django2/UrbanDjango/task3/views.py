from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    zero = 'Main Page'
    first = 'Market'
    second = 'Trash'
    context = {
        'zero': zero,
        'first': first,
        'second': second,
    }
    return render(request, "third_task/index.html", context)

def market(request):
    buy = 'BUY'
    text = 'Back to main page'
    context = {
        'buy': buy,
        'text': text,
    }
    return render(request, "third_task/first_page.html", context)

def trashcan(request):
    text = 'Back to main page'
    context = {
        'text': text,
    }
    return render(request, "third_task/second_page.html", context)