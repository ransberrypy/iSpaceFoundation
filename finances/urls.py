from django.urls import path,include
from .views import StockList
urlpatterns = [
     path('inventory', StockList.as_view(), name='stocklevel')
]