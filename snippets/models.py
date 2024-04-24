
from django.db import models

LANGUAGE_CHOICES = [('abap', 'ABAP'), ('abnf', 'ABNF'), ('ada', 'Ada'), ('adl', 'ADL'), ('agda', 'Agda'), ('python', 'Python')]
STYLE_CHOICES = [('algol', 'algol'), ('algol_nu', 'algol_nu'), ('friendly', 'friendly')]
BOOK_TYPES = [('science', 'science'), ('fiction', 'fiction')]

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created']


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(choices=BOOK_TYPES, default='science', max_length=100)
