# task_manager/views.py

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import RegisterForm, UpdateForm


# Получаем актуальную модель пользователя (поддерживает кастомные модели)
User = get_user_model()

class IndexView(TemplateView):
    template_name = 'index.html'


class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/create.html'
    success_url=reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'

class UserUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:list')
    success_message = 'Пользователь успешно изменен'

    def test_func(self): return self.request.user.pk == self.kwargs['pk']

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения')
        return redirect('users:list')

class UserDeleteView(SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:list')
    success_message = 'Пользователь успешно удален'
    def test_func(self): return self.request.user.pk == self.kwargs['pk']
    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения')
        return redirect('users:list')

class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = 'Вы залогинены'

class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)