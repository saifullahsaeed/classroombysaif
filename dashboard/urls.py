from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('logout/',views.logoutUser,name="logout"),
    path('choseaccount/',views.select_account,name="chose_acc"),
    path('account/shift/',views.shift,name="shift"),
    path('account/',views.account,name="account"),
    path('joinclass/<str:usern>/classid=<slug:key>/', views.join_student,name="join_class"),
    path('joinclass/<int:accept>/<str:usern>/classid=<slug:key>/', views.join_students,name="join_class")
]
