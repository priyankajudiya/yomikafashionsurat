from django.contrib.auth.models import User
from .models import Cart


def cartCount(request):
    c = 0
    try:
        obj = Cart.objects.filter(user = request.user)
        for x in obj:
            c += 1
    except:pass

    return {'cartCount':c}

def cartTotal(request):
    total = []
    try:
        obj = Cart.objects.filter(user=request.user)
        for x in obj:
            total.append(x.product_id.price*x.product_qty)
            #print(x.product_id.price, x.product_qty,x.product_id.price*x.product_qty)
    except:
        pass

    return {'cartTotal': sum(total)}
