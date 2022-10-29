from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, UpdateView
from authapp.models import User
from authapp.forms import CustomUserChangeForm, CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'authapp/login.html'
    extra_context = {
        'title': 'Вход пользователя'
    }

    def form_valid(self, form):
        ret = super().form_valid(form)

        message = ("Вход успешный!<br>Здраствуйте, %(username)s") % {
            "username": self.request.user.get_full_name()
            if self.request.user.get_full_name()
            else self.request.user.get_username()
        }
        messages.add_message(self.request, messages.INFO, mark_safe(message))
        return ret

    def form_invalid(self, form):
        messages.add_message(self.request, messages.WARNING, 'Неправильное имя пользователя или пароль!')
        return self.render_to_response(self.get_context_data(form=form))


class CustomLogoutView(LogoutView):
    template_name = 'authapp/login.html'


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('authapp:login')
    template_name = 'authapp/password_change_form.html'


class CreateUserView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('authapp:login')


class EditUserView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'authapp/edit.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('authapp:edit', args=[self.request.user.pk])
