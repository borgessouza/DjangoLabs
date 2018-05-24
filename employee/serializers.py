from .models import Employee
from rest_framework import serializers


class employee_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'department', 'create_date')