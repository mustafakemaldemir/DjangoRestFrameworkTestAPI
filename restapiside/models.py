from django.db import models
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    biography = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Article(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=150)
    comment = models.CharField(max_length=150)
    text = models.TextField()
    city = models.CharField(max_length=150)
    activity_status = models.BooleanField(max_length=150)
    published_date = models.DateField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True) #otomatik oluşturduktan sonra değişiklik yapılamaz
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Author: {self.author}, Article Title: {self.title}"