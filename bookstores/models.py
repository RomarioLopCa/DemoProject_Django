from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name + " - " + str(self.age) + " años"


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

    def __str__(self):
        return self.name + " - " + str(self.num_awards) + " premios"


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()

    def __str__(self):
        return self.name + " - " + str(self.pages) + " páginas \n" \
                                                     "Autores: {" + self.authors.all() + "\n" \
                                                                                                    "Publisher: " \
               + self.publisher


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()
