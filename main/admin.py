from django.contrib import admin
from main.models import ListItem, ShoppingList
# Register your models here.


class ListItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'tick', 'shopping_list')
    list_filter = ('tick', 'shopping_list')
admin.site.register(ListItem, ListItemAdmin)

class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('list_name',)
    list_filter = ('list_owner',)
admin.site.register(ShoppingList, ShoppingListAdmin)