from django.contrib import admin
from .models import Order, OrderLineItem


# Register your models here.
class OrderLineItemAdminInline(admin.TabularInline):
    # can add items to an order but not change
    # the automatically calculated line total
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    # make specific fields un-editable
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total')

    fields = ('order_number', 'date', 'first_name', 'last_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total')

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'order_total', 'delivery_cost',
                    'grand_total')

    # set most recent orders at the top
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
