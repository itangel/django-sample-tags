from django.conf.urls import patterns, url

from .views import IndexView, BookListView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^books/$', BookListView.as_view(), name="book_list"),
]
