from django.shortcuts import render
from django.views.generic import ListView
from .bookkeeper.stocks import Stock

# Create your views here.
class StockList(ListView):
    template_name='finance/stock.html'
    queryset = Stock.objects.all()