from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Section, Reader, Book, Ticket


def home(request):
    return render(request, 'home.html')

def sections(request):
    return render(request, 'sections.html', {'sections': Section.objects.all()})

def books(request):
    return render(request, 'books.html', {'books': Book.objects.all()})

@csrf_protect
def tickets(request):
    if request.method == 'POST':
        reader_id = request.POST['reader_id']
        book_id = request.POST['book_id']
        issue_date = request.POST['issue_date']
        return_date = request.POST['return_date']
        Ticket(reader_id=Reader.objects.get(pk=reader_id), book_id=Book.objects.get(pk=book_id),
               issue_date=issue_date, return_date=return_date).save()
        return render(request, 'tickets.html', {
            'tickets': Ticket.objects.all(),
            'readers': Reader.objects.all(),
            'books': Book.objects.all(),
        })
    else:
        return render(request, 'tickets.html', {
            'tickets': Ticket.objects.all(),
            'readers': Reader.objects.all(),
            'books': Book.objects.all(),
        })

def readers(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']
        street = request.POST['street']
        house_number = request.POST['house_number']
        apartment_number = request.POST['apartment_number']
        passport = request.POST['passport']
        Reader(name=name, surname=surname, patronymic=patronymic, street=street, house_number=house_number,
               apartment_number=apartment_number, passport=passport).save()
        return render(request, 'readers.html', {'readers': Reader.objects.all()})
    else:
        return render(request, 'readers.html', {'readers': Reader.objects.all()})

def report_about_count_book(request):
    pass

def report_about_reading_book(request):
    pass