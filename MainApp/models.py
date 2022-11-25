from django.db import models
from django.contrib.auth.models import User

LANGS = [
    ("py", "python"),
    ("js", "javascript"),
    ("cpp", "C++"),
]


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANGS)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='snippets',
                             blank=True, null=True)
    public = models.BooleanField(editable=True, default=True)

    def __str__(self):
        return f"{self.id}. {self.name} by {self.user}"


class Comment(models.Model):
    text = models.TextField(max_length=2000)
    creation_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')
    snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE, related_name='comments')
