from django.db import models


class Note(models.Model):
    title = models.CharField('заголовок', max_length=120)
    text = models.TextField('текст', blank=True)
    created_at = models.DateTimeField('создано', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'

    def __str__(self):
        return self.title
