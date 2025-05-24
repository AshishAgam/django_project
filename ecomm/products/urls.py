from django.urls import path
from products.views import get_products, short_description

urlpatterns = [
    path('<slug>/', get_products, name="get_products"),
    path('short-description.html', short_description, name='short-description'),
]
