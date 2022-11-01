from django.db import models
from authapp.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст заметки', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Обновлено')
    completed = models.BooleanField(default=False, verbose_name='Выполнено')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')
    todo_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name='Пользователь заметки')
    important = models.BooleanField(default=False, verbose_name='Важность заметки')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['todo_user', '-created_at', 'important', 'title']

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def __str__(self):
        return f'{self.todo_user} {self.title} {self.created_at}'
