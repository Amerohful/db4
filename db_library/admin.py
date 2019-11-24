from django.contrib import admin
from .models import Section, Reader, Book, Ticket


class SectionAdmin(admin.ModelAdmin):
    pass


class ReaderAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


class TicketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Section, SectionAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Ticket, TicketAdmin)
