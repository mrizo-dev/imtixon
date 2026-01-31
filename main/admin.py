from django.contrib import admin
from .models import Student, Reja

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('ism', 'yosh', 'kurs')
    list_display_links = ('ism',)
    search_fields = ('ism',)
    list_filter = ('kurs',)

@admin.register(Reja)
class RejaAdmin(admin.ModelAdmin):
    list_display = ('sarlavha', 'sana', 'bajarildi', 'student')
    list_display_links = ('sarlavha',)
    list_filter = ('bajarildi',)
    search_fields = ('sarlavha',)
    autocomplete_fields = ('student',)