import os, django
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nta_library.settings")
django.setup()
from books.models import Book, Borrower
from faker import Faker

fakegen = Faker()
def populate(N=5):
    rows = []
    for entry in range(N):
        fake_name = fakegen.name()
        fake_auther = fakegen.name()
        fake_type = fakegen.name()
        fake_isbn = fakegen.zipcode()
        fake_copies = fakegen.zipcode()
        fake_issue_date = fakegen.date()
        fake_date = fakegen.date()
        fake_out = fakegen.boolean()
        # New entry
        boooooks = Book.objects.get_or_create(name=fake_name,auther=fake_auther,type=fake_type,isbn = fake_isbn,copies=fake_copies, 
        issue_date=fake_issue_date,out=fake_out  )[0]
        borrrrrowerrrr= Borrower.objects.get_or_create(borrower_book = boooooks, name= fake_name, 
        department = fake_name, borrow_date = fake_date,return_date = fake_date, blacklisted = fake_out)[0]
        rows.append(boooooks)
    return rows

populate(5)