from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

class Book(models.Model):
    caption = models.CharField(max_length=255)
    brief = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    store_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.caption}'
