from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import UserForm, AuthorForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from webapp.models import Author


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