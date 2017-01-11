from django.db import models

# Create your models here.

class Unit(models.Model):
    unit_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unit_name
    
class Expense_Type(models.Model):
    expense_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expense_name

class Expense(models.Model):
    payer = models.ForeignKey(Unit, related_name="payer", on_delete=models.CASCADE)
    payee = models.ForeignKey(Unit, related_name="payee", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=0)
    type = models.ForeignKey(Expense_Type, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)
    note = models.CharField(max_length=200, blank=True)
    pay_day = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s: %d" %(self.payer, self.payee, self.amount)
