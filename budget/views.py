from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import django_tables2 as tables
import itertools

from .models import Expense
from .models import Expense

class EditColumn(tables.Column):
    def render(self, value):
        return format_html('<a href="budget/new/">Edit/{}</a>', value)

class ExpenseTable(tables.Table):
    no = tables.Column(empty_values=())

    def render_no(self):
        return '%d' % next(self.counter)

    def __init__(self, *args, **kwargs):
        super(ExpenseTable, self).__init__(*args, *kwargs)
        self.counter = itertools.count()
    
    class Meta:
        model = Expense
        fields = ('no', 'payer', 'payee', 'amount', 'expense_name', 'pay_day', 'description', 'note')
        attrs = {'class': 'table table-striped table-bordered table-hover'}

def index(request):
    expenses_list = Expense.objects.all()
    table = ExpenseTable(expenses_list)
    return render(request, 'budget/index.html', {'table': table, })

def new(request):
    return render(request, 'budget/new.html', {})
