from django.urls import path
from .views import UserDetailView, UserUpdateView, AuthorListView, AuthorCreateView, AuthorDetailView, AuthorUpdateView, \
    AuthorDeleteView, BookCreateView, BookDeleteView, BookDetailView, BookListView, BookUpdateView, ReviewCreateView, \
    ReviewDeleteView, ReviewUpdateView, BookShelfView, BookShelfDeleteView

app_name = 'webapp'

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_details'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user_update'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_details'),
    path('author/<int:pk>/update', AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete', AuthorDeleteView.as_view(), name='author_delete'),
    path('', BookListView.as_view(), name='book_list'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_details'),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
    path('book/<int:pk>/review/create/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review_delete'),
    path('book/<int:pk>/add', BookShelfView.as_view(), name='add_book'),
    path('book/<int:pk>/remove', BookShelfDeleteView.as_view(), name='remove_book'),
]
