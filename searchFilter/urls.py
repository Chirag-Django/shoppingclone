from django.urls import path
from . import views


app_name='searchFilter'
urlpatterns = [
    path('product/search/',views.searchProduct,name='search_product'),
]


