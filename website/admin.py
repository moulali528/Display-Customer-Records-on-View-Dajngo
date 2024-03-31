from django.contrib import admin
from .models import CustomerRecords, CustomerDeletedRecords
# Register your models here.

admin.site.register(CustomerRecords)
admin.site.register(CustomerDeletedRecords)
