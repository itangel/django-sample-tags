from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from .models import Book


class IndexView(CreateView):
	model = Book
	success_url = reverse_lazy("book_list")
	template_name = "main/index.html"
	fields = ('title', 'tags')


class BookListView(ListView):
	model = Book
	template_name = "main/list.html"
	
