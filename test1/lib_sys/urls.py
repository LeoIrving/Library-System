
from lib_sys import views
from django.urls import path

urlpatterns = [
    path('books/',views.show_books),
    path('books/<int:bid>',views.detail),
    path('authors/',views.show_authors),
    path('authors/<int:aid>',views.authorinfo),
    path('lenders/',views.show_lenders),
    path('lenders/<int:lid>',views.lenderinfo),
    path('borrowers/',views.show_borrowers),
    path('borrowers/<int:boid>',views.borrowerinfo),
]