from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import CustomUser, Tag, Expense, Goal
from .serializers import (
    CustomUserSerializer, 
    TagSerializer, 
    ExpenseSerializer, 
    GoalSerializer,
    RegisterUserSerializer,
)

# Read only views using serializers
class ReadUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
class ReadUser(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
class ReadTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
class ReadTag(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
class ReadExpenseList(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
class ReadExpense(generics.RetrieveAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
class ReadGoalList(generics.ListAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
class ReadGoal(generics.RetrieveAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]
    
    def post(self, req):
        register_serializer = RegisterUserSerializer(data = req.data)
        if register_serializer.is_valid():
            newuser = register_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(
            register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)