from .models import Employee
from rest_framework import serializers


class employee_serializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=50)
    department = serializers.CharField(max_length=50)
    email = serializers.EmailField()


    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.department = validated_data.get('department', instance.department)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
