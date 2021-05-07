from django.http import HttpResponse, response
from django.contrib import messages
from auths.models import User_data
from dashboard.models import class_db
from classes.models import Students
from classes.views import inclass, is_student
from django.shortcuts import redirect


class class_security:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request,**key):
        
        response = self.get_response(request)
        return response
