from django.db import models

# Create your models here.
STATUS_CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано'),
]


class Entry(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя автора')
    email = models.EmailField(null=False, blank=False, verbose_name='Почта автора')
    text = models.TextField(null=False, blank=False, verbose_name='Текст записи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name='Статус'
    )

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        db_table = 'entry'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-created_at']