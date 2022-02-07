from datetime import date
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username

class Tag(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Expense(models.Model):
    cost = models.DecimalField(max_digits=14, decimal_places=2)
    date = models.DateField(default=date.today)
    note = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='expenses')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id

class Goal(models.Model):
    goal = models.DecimalField(max_digits=14, decimal_places=2)
    description = models.CharField(max_length=300)
    month = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id