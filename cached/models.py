from datetime import date
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = 'customuser'
        verbose_name_plural = 'customusers'

class Tag(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tags')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Expense(models.Model):
    cost = models.DecimalField(max_digits=14, decimal_places=2)
    date = models.DateField(default=date.today)
    note = models.CharField(max_length=300)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='expenses')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='expenses')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id

class Goal(models.Model):
    goal = models.DecimalField(max_digits=14, decimal_places=2)
    description = models.CharField(max_length=300)
    month = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='goals')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id