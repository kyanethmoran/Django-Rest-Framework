import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    #the field name is the model field that we want to filter by, and iexact is how you make the filter
    #case insensitive (good for lower or upper case format of the desired lookup field)
    designation = django_filters.CharFilter(field_name='designation', lookup_expr= 'iexact')
    emp_name = django_filters.CharFilter(field_name= 'emp_name', lookup_expr= 'iexact')
    id = django_filters.NumberFilter(field_name= 'id')
    #to be able to search within the range of emp_id we need to modify how id_min & id_max work
    #pass a custom function to the method param that will allow us to isolate the numbers only
    #within emp_id, label parameter will change the label about the input field in the filter popup
    id_min = django_filters.CharFilter(method= 'filter_by_emp_id_range', label = "From EMP ID")
    id_max = django_filters.CharFilter(method= 'filter_by_emp_id_range', label = 'To EMP ID')
    

    class Meta:
        model = Employee
        fields = ['designation','emp_name', 'id', 'emp_id', 'id_min', 'id_max']

    #custom function to isolate the emp_id numbers to be able to filter a range of them
    def filter_by_emp_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte = value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte = value)
        return queryset