from django.shortcuts import render, redirect

# Create your views here.

def offert(request):
    items = []
    data = {"items": items}
    return render(request, "offert.html", data)

def basket(request):
    items = []
    data = {"items": items}
    return render(request, "basket.html", data)

def order(request):
    data = {}
    return render(request, "order.html", data)

def order_basket(request):
    return redirect('basket')