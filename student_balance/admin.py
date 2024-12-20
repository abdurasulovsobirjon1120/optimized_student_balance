from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Student, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance')
    search_fields = ('name',)
    ordering = ('name',)

    def save_model(self, request, obj, form, change):
        """
        Kategoriya saqlanganda boshqa qo'shimcha ishlov kerak bo'lsa shu yerga yozilishi kerak.
        """
        obj.save()


admin.site.register(Category, CategoryAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'start_date', 'category', 'balance', 'status', 'update_balances_button')
    ordering = ('-id',)
    search_fields = ('first_name', 'last_name')

    def update_balances_button(self, obj):
        url = reverse('update_balances')
        return format_html(f'<a class="button" href="{url}">Update Balances</a>')
    update_balances_button.short_description = 'Update Balances'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            if obj.category:
                obj.balance = 0
        obj.save()


admin.site.register(Student, StudentAdmin)