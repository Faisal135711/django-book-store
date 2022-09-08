from basket.session import BasketSession

def basket(request):
    return {'basket': BasketSession(request)}