from django.contrib import admin
from .models import User, Expense, Tag, Goal

admin.site.register(User)
admin.site.register(Expense)
admin.site.register(Tag)
admin.site.register(Goal)