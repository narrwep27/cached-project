from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser, Expense, Tag, Goal

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        extra_kwargs = { 'password': {'write_only': True} }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user_id'] = self.user.id
        return data

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'is_superuser', 'expenses', 'tags', 'goals')
        depth = 1

class TagSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = CustomUser.objects.all(),
        many = False
    )
    class Meta:
        model = Tag
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = CustomUser.objects.all(),
        many = False
    )
    tag = serializers.PrimaryKeyRelatedField(
        queryset = Tag.objects.all(),
        many = False
    )
    class Meta:
        model = Expense
        fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = CustomUser.objects.all(),
        many = False
    )
    class Meta:
        model = Goal
        fields = '__all__'