# task_manager/views.py

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView

User = get_user_model()

class IndexView(TemplateView):
    template_name = 'index.html'

class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = 'Вы залогинены'

class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)