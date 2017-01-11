from django.contrib import admin

from .models import Expense, Expense_Type, Unit

admin.site.register(Expense)
admin.site.register(Unit)
admin.site.register(Expense_Type)
