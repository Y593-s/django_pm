from django.urls import path, include
from django.urls import path, include
from accounts.forms import UserLoginForm
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('', include('django.contrib.auth.urls'))
]