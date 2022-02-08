from dataclasses import fields
from rest_framework import serializers
from .models import CustomUser, Expense, Tag, Goal

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'is_superuser', 'is_staff', 'expenses', 'tags', 'goals')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'user', 'expenses')

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'cost', 'date', 'note', 'user', 'tag')

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'goal', 'description', 'month', 'user')