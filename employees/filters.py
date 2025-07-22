import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    #the field name is the model field that we want to filter by, and iexact is how you make the filter
    #case insensitive (good for lower or upper case format of the desired lookup field)
    designation = django_filters.CharFilter(field_name='designation', lookup_expr= 'iexact')

    class Meta:
        model = Employee
        fields = ['designation']