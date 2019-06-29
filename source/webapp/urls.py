from django.urls import path
from .views import UserDetailView, UserUpdateView, AuthorListView

app_name = 'webapp'

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_details'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user_update'),
    path('', AuthorListView.as_view(), name='author_list'),
]
