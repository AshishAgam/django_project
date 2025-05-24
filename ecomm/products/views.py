from django.shortcuts import render

# Create your views here.
def get_products(request, slug):
    return render(request, "product-layout-1.html")

def short_description(request):
    return render(request, "short-description.html")