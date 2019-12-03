import io
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.db import connection
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
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


@csrf_protect
def reports(request):
    return render(request, 'reports.html', {'readers': Reader.objects.all()})


def report_about_count_book(request):
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

    doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))
    # container for the 'Flowable' objects
    elements = []
    cursor = connection.cursor()
    cursor.execute('select r.name, r.surname, count(t.issue_date) '
                   'from db_library_ticket t, db_library_reader r, db_library_book b '
                   'where t.return_book is False and r.id = t.reader_id_id and b.id = t.book_id_id '
                   'group by r.name, r.surname '
                   'order by min(t.issue_date);')
    reader = [('Имя', 'Фамилия', 'Колличество книг на руках')] + [x[1] for x in enumerate(cursor.fetchall())]
    tblstyle = TableStyle([('FONT', (0, 0), (-1, -1), 'DejaVuSerif', 12)])
    t = Table(reader)
    t.setStyle(tblstyle)
    elements.append(t)
    # write the document to disk
    doc.build(elements)
    try:
        return FileResponse(open('simple_table.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


def report_about_reading_book(request):
    reader_id = 1
    if request.method == 'POST':
        reader_id = request.POST.get('reader_id', 1)
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

    doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))
    # container for the 'Flowable' objects
    elements = []
    cursor = connection.cursor()
    cursor.execute(f'select b.book_name, t.issue_date from db_library_ticket t, db_library_book b ' \
                   f'where t.reader_id_id = {reader_id} and t.return_book is True and b.id = t.book_id_id ' \
                   f'order by t.issue_date;')
    reader = [('Название книги', 'Дата выдачи')] + [x[1] for x in enumerate(cursor.fetchall())]
    tblstyle = TableStyle([('FONT', (0, 0), (-1, -1), 'DejaVuSerif', 12)])
    t = Table(reader)
    t.setStyle(tblstyle)
    elements.append(t)
    # write the document to disk
    doc.build(elements)
    try:
        return FileResponse(open('simple_table.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
