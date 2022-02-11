from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser, Tag, Expense, Goal
from .serializers import (
    GoalSerializer,
    RegisterUserSerializer,
    CustomTokenObtainPairSerializer,
    CustomUserSerializer,
    TagSerializer, 
    ExpenseSerializer,
    GoalSerializer
)

class CreateCustomUser(APIView):
    permission_classes = [AllowAny]
    def post(self, req):
        register_serializer = RegisterUserSerializer(data = req.data)
        if register_serializer.is_valid():
            newuser = register_serializer.save()
            if newuser:
                return Response(register_serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ListUsers(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class RetrieveUser(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class DestroyUser(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    def destroy(self, req, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={'msg':'User destroyed'}, status=status.HTTP_200_OK)

class CreateTag(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class UpdateDestroyTag(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    def destroy(self, req, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={'msg':'Tag destroyed'}, status=status.HTTP_200_OK)

class CreateExpense(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class UpdateDestroyExpense(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    def destroy(self, req, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={'msg':'Expense destroyed'}, status=status.HTTP_200_OK)

class CreateGoal(generics.CreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class UpdateDestroyGoal(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    def destroy(self, req, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={'msg':'Goal destroyed'}, status=status.HTTP_200_OK)