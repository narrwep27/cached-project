from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from .models import CustomUser, Tag, Expense, Goal
from .serializers import (
    GoalSerializer,
    RegisterUserSerializer,
    CustomUserSerializer, 
    TagSerializer, 
    ExpenseSerializer,
    GoalSerializer
)

# Read only views using serializers
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

class ListUsers(generics.ListAPIView):
    permission_classes = [IsAdminUser]
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

class RetrieveUser(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CreateTag(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # def create(self, req, *args, **kwargs):
    #     user_id = kwargs.get('user_id')
    #     serializer = self.get_serializer(data=req.data, context={ "user_id": user_id })
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
    # def create(self, req, *args, **kwargs):
    #     user_id = kwargs.get('user_id')
    #     tag_id = kwargs.get('tag_id')
    #     serializer = self.get_serializer(data=req.data, context={
    #         'user_id': user_id,
    #         'tag_id': tag_id
    #     })
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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