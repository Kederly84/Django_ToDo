from django.contrib import admin
from todo.models import Todo


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('todo_user', 'title', 'created_at', 'deleted')
    list_per_page = 10
    list_filter = ('todo_user', 'title', 'created_at', 'deleted')
    search_fields = ('todo_user', 'title', 'created_at', 'deleted')
    show_full_result_count = False
