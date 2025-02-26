from django.shortcuts import render
from django.http import Http404
from .models import Product
def Home(request):
    products = Product.objects.all()
    return render(request ,"index.html" , {"products" : products})

def cart(request):
    return render(request, "cart.html")

def product_details(request , id) :
    products = Product.objects.all()
    try:
        product = Product.objects.get(id = id)
    except:
        raise Http404("product not found")
    return render(request , "productDetails.html" ,{"products" : products  , "product" : product} )

def deleteProductfromCart(request,id):
    Product= selctedproducts.objects.get(id=id)
    property.delete()
    return redirect('products:cart')
def addToCart(requset,id):
    product = Product.objects.get(id=id)
    selectedproducts.objects.create(id=id, imge= product.imge, name= product.name, price= product.price, totalprice= product.price)
    return redirect('products:cart')

def product_details(request , id) :
    products = Product.objects.all()
    try:
        product = Product.objects.get(id = id)
    except:
        raise Http404("product not found")
    return render(request , "productDetails.html" ,{"products" : products  , "product" : product} )