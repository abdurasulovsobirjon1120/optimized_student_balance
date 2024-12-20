from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=50)
    balance = models.IntegerField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=400)
    start_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    balance = models.IntegerField(default=0)
    status = models.CharField(max_length=30, default='to\'langan')

    def update_balance(self):
        if self.category:
            months_passed = (date.today().year - self.start_date.year) * 12 + (date.today().month - self.start_date.month)
            self.balance = -(months_passed * self.category.balance)
            self.status = 'qarzdor' if self.balance < 0 else 'to\'langan'
            self.save()