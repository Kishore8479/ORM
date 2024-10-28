# Ex02 Django ORM Web Application
## Date: 28/10/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2024-10-28 200825.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

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

admin.py

from django.contrib import admin
from .models import BankLoan,BankLoanAdmin
admin.site.register(BankLoan,BankLoanAdmin)

```


## OUTPUT

![alt text](<Screenshot 2024-10-28 195557.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
