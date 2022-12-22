from django.urls import path
from .views import RegisterUserView, activate_view, LoginView, LogoutView


urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('activate/<str:activation_code>/', activate_view),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    
]