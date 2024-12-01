from django.shortcuts import render


# Create your views here.
def main_page(requset):
    return render(requset, 'fourth_task/index2.html')


def store_games(requset):
    context = {'games': ['GTA 5', 'GTA 6', 'GTA 7']}
    return render(requset, 'fourth_task/first_page.html', context)



def cart_page(request):
    cart_items = {
        'GTA 5': {'price': 1500, 'quantity': 1},
        'GTA 6': {'price': 2000, 'quantity': 1},
    }
    total = sum(item['price'] * item['quantity'] for item in cart_items.values())
    discount = 0.1 if total > 200 else 0
    final_total = total - (total * discount)
    discount_percent = discount * 100
    return render(request, 'fourth_task/second_page.html', {
        'cart_items': cart_items,
        'total': total,
        'final_total': final_total,
        'discount_percent': discount_percent
    })
