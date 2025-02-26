from django.urls import path 
from . import views
app_name = "products"

urlpatterns = [

    path("home/" , views.Home) , 
    path("cart/" , views.cart),
    path("<int:id>/" ,  views.product_details , name="product_details"),
    path("adds/<int:id>/" , views.addToCart , name="add_product"),
    
]