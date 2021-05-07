from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login,name="login"),
    path('register/',views.register,name="register"),
    path('choose/<slug:type>/',views.choose_account,name="choose"),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),  
]