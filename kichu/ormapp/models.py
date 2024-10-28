
from django.db import models
from django.contrib import admin
class BankLoan(models.Model):
    borrower_name = models.CharField(max_length=100)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField()
    loan_term = models.IntegerField()  
    loan_number = models.IntegerField(primary_key="loan_number")
        

class BankLoanAdmin(admin.ModelAdmin):
    list_display = ('borrower_name', 'loan_amount', 'interest_rate', 'loan_term', 'loan_number')