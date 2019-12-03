from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('readers/', views.readers, name='readers'),
    path('reports/', views.reports, name='reports'),
    path('books/', views.books, name='books'),
    path('sections/', views.sections, name='sections'),
    path('tickets/', views.tickets, name='tickets'),
    path('report_about_count_book/', views.report_about_count_book, name='report_about_count_book'),
    path('report_about_reading_book/', views.report_about_reading_book, name='report_about_reading_book'),
]