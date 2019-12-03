from django.db import models


class Section(models.Model):
    section_name = models.CharField(max_length=45)

    def __str__(self):
        return self.section_name


class Reader(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)
    apartment_number = models.IntegerField()
    passport = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic}'


class Book(models.Model):
    section_code = models.ForeignKey(Section, on_delete=models.PROTECT)
    book_name = models.CharField(max_length=100)
    fio_author = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.book_name


class Ticket(models.Model):
    reader_id = models.ForeignKey(Reader, on_delete=models.PROTECT)
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    issue_date = models.DateField()
    return_date = models.DateField()
    return_book = models.BooleanField(default=False)
