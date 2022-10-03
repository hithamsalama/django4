from django import forms
from .models import Book, Borrower

#    class Register_a_book(forms.Form):
#        name = forms.CharField()
#        auther = forms.CharField()
#        type = forms.CharField()
#        isbn = forms.IntegerField()
#        copies = forms.IntegerField()
#        issue_date = forms.DateField(widget=forms.SelectDateWidget)
#        out = forms.BooleanField()

class NewBook_form(forms.ModelForm):
    class Meta():
        model = Book
        fields = '__all__'

