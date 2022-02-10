from multiprocessing import context
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from .models import CustomUser, Tag, Expense, Goal
from .serializers import (
    RegisterUserSerializer,
    CustomUserSerializer, 
    TagSerializer, 
    ExpenseSerializer,
)

# Read only views using serializers
class CreateCustomUser(APIView):
    permission_classes = [AllowAny]
    
    def post(self, req):
        register_serializer = RegisterUserSerializer(data = req.data)
        if register_serializer.is_valid():
            newuser = register_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(
            register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListUsers(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

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