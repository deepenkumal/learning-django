from django.urls import reverse_lazy
from .forms import SignupForm
from .decorators import unathenticated_user
from django.views import generic
# Create your views here.



class  SignupView(generic.CreateView):
    
    template_name = 'users/signup.html'
    form_class = SignupForm
    
    success_url = reverse_lazy('login')

class ProfileView(generic.TemplateView):
    template_name = 'users/profile.html'

