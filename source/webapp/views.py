from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import UserForm, AuthorForm, BookForm, ReviewForm
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from webapp.models import Author, Book, Review


class UserDetailView(DetailView):
    template_name = 'user_details.html'
    model = User


class UserUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = User
    template_name = 'user_update.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('webapp:user_details', kwargs={'pk': self.object.pk})

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if user != self.request.user:
            return HttpResponseRedirect(reverse('webapp:user_details', kwargs={'pk': pk}))
        return super().get(request, pk=pk)

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user == self.get_object().author


class AuthorListView(ListView):
    template_name = 'author_list.html'
    model = Author


class AuthorCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'author_create.html'
    form_class = AuthorForm
    model = Author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AuthorDetailView(DetailView):
    template_name = 'author_details.html'
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context


class AuthorUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'author_update.html'
    form_class = AuthorForm
    model = Author

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


class AuthorDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'author_delete.html'
    model = Author
    success_url = reverse_lazy('webapp:author_list')

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book


class BookCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'book_create.html'
    form_class = BookForm
    model = Book

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BookDetailView(DetailView):
    template_name = 'book_details.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all().order_by('-created_at')
        return context


class BookUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'book_update.html'
    form_class = BookForm
    model = Book

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


class BookDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'book_delete.html'
    model = Book
    success_url = reverse_lazy('webapp:book_list')

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


class ReviewListView(ListView):
    template_name = 'review_list.html'
    model = Review


class ReviewCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'partial/review_form.html'
    form_class = ReviewForm
    model = Review

    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        form.instance.book = book
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewDetailView(DetailView):
    template_name = 'review_detail.html'
    model = Review


class ReviewUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'review_update.htmll'
    form_class = ReviewForm
    model = Review

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user == self.get_object().author


class ReviewDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'review_delete.html'
    model = Review
    success_url = reverse_lazy('webapp:book_list')

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user == self.get_object().author

