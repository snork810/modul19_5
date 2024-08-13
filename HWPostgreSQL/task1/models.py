from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NON', 'Non-Fiction'),
        ('SCI', 'Science Fiction'),
        ('FAN', 'Fantasy'),
        ('MIS', 'Mistery'),
        ('THR', 'Thriller'),
        ('ROM', 'Romance'),
        ('HIS', 'Hustorical')
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField()
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, default='FIC')

    def __str__(self):
        return self.title


class Buyer(models.Model):
    Name = models.CharField(max_length=100)
    balance = models.IntegerField()

    def __str__(self):
        return self.Name
