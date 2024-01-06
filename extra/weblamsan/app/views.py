from django.shortcuts import render

from app.blockchain_web3.product_provider import ProductProvider
from app.blockchain_web3.traceability import TraceabilityProvider


def home(requets):
    products = ProductProvider().get_product_all()
    return render(requets, 'home.html', context={"products": products})


def about(requets, pk):
    product = ProductProvider().get_product_by_id(pk)
    return render(requets, "about.html", context={"product": product})


def traceability(requets, pk):
    result = TraceabilityProvider().get_info_product(pk)
    return render(requets, "traceability.html", context={"info": result})