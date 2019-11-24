from django.shortcuts import render
from django.http import HttpResponse
from .models import Section, Reader, Book, Ticket


def home(requests):
    return render(requests, 'home.html')

def sections(requests):
    return render(requests, 'sections.html', {'sections': Section.objects.all()})

def books(requests):
    return render(requests, 'books.html', {'books': Book.objects.all()})

def tickets(requests):
    return render(requests, 'tickets.html', {'tickets': Ticket.objects.all()})

def readers(requests):
    return render(requests, 'readers.html', {'readers': Reader.objects.all()})