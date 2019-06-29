from django.urls import path
from .views import UserDetailView, UserUpdateView, AuthorListView, AuthorCreateView, AuthorDetailView

app_name = 'webapp'

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_details'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user_update'),
    path('', AuthorListView.as_view(), name='author_list'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_details'),
]
