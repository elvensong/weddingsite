from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import django_tables2 as tables
from .models import Expense

from .models import Expense

class EditColumn(tables.Column):
    def render(self, value):
        return format_html('<a href="budget/new/">Edit/{}</a>', value)

class ExpenseTable(tables.Table):
    normal = tables.Column()
    
    
    class Meta:
        model = Expense

def index(request):
    expenses_list = Expense.objects.all()
    table = ExpenseTable(expenses_list)
    return render(request, 'budget/index.html', {'table': table, })

def new(request):
    return render(request, 'budget/new.html', {})
