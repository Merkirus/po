from django.shortcuts import render

# Create your views here.

def offert(request):
    items = []
    data = {"items": items}
    return render(request, "offert.html", data)

def basket(request):
    items = []
    data = {"items": items}
    return render(request, "basket.html", data)