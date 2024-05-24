from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
# Create your views here.
class MyAccountView(TemplateView):
    template_name = 'index.html'
    
class SignUpView(SuccessMessageMixin,CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('account_view')
    form_class = UserRegisterForm
    success_message = 'Your account has been signed up'

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('account_view')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    

    