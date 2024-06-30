from django.contrib import admin

from companycrudapp.models import Company


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['companyname', 'ceo', 'headquarters', 'foundedyear','typeofcompany','primaryindustry']


admin.site.register(Company, CompanyAdmin)
