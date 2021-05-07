from django.urls import path
from channels.routing import route_pattern_match
from . import views

urlpatterns = [
    path('add/', views.add,name = "create_class"),
    path('upload_assignment/', views.upload_assignment,name = "upload_assignment"),
    path('lactures/classid=<slug:key>', views.lactures,name = "lactures"),
    path('lacture/lacture_id=<slug:id>/classid=<slug:key>', views.lacture,name = "lacture"),
    path('classroom/classid=<slug:key>',views.classroom,name="class_student"),
    path('class-admin/classid=<slug:key>',views.class_admin,name="class_Teacher"),
    path('assignments/classid=<slug:key>',views.assignment,name="class_assignment"),
    path('quiz/classid=<slug:key>',views.quizz,name="class_quizz"),
    path('announcement/classid=<slug:key>',views.announcements,name="announcement"),
    path('comment/',views.comments,name="lactureComment")
]