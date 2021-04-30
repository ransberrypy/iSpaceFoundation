from django.contrib import admin
from .bookkeeper.sales import Invoice
from .bookkeeper.accounting import Transaction
from .bookkeeper.purchases import Merchant, Receipt
from .bookkeeper.stocks import Stock

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display=['customer_details','slug','code', 'invoice_doc']
    search_fields = ['customer_details','slug','name','code','description']
    list_per_page = 30

admin.site.register(Invoice, InvoiceAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['date','description','code','amount','account','category','doc','is_match']
    list_editable = ['is_match']
    search_fields=['code','description','amount','account']
    list_per_page = 30
    list_display_links = ['date','description','code']

admin.site.register(Transaction,TransactionAdmin)


admin.site.register(Receipt)
admin.site.register(Merchant)
admin.site.register(Stock)

