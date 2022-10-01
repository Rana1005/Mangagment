from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import *
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name="dispatch")
# @csrf_exempt
class RegisterParent(View):
    def post(self, request):
        print("post method call")
        return JsonResponse({"status":2})


