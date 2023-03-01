from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentID','DepartmentName')


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeID','EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')