from django import forms
from .models import Book


class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.IntegerField()
    qty = forms.IntegerField()
    author = forms.CharField(max_length=100)
    is_published = forms.BooleanField()



class Bform(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        # fields = ('name', 'price', 'qty')  # -- list or tuple -- both accepted



