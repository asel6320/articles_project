from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
import json

@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == 'GET':
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(permitted_methods=["GET"])
def validate_numbers(data):
    try:
        A = float(data.get('A'))
        B = float(data.get('B'))
        return A, B, None
    except (ValueError, TypeError):
        return None, None, JsonResponse({"error": "Invalid input, please provide numbers."}, status=400)

@require_http_methods(["POST"])
def add(request):
    try:
        data = json.loads(request.body)
        A, B, error = validate_numbers(data)
        if error:
            return error
        return JsonResponse({"answer": A + B})
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data."}, status=400)

@require_http_methods(["POST"])
def subtract(request):
    try:
        data = json.loads(request.body)
        A, B, error = validate_numbers(data)
        if error:
            return error
        return JsonResponse({"answer": A - B})
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data."}, status=400)

@require_http_methods(["POST"])
def multiply(request):
    try:
        data = json.loads(request.body)
        A, B, error = validate_numbers(data)
        if error:
            return error
        return JsonResponse({"answer": A * B})
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data."}, status=400)

@require_http_methods(["POST"])
def divide(request):
    try:
        data = json.loads(request.body)
        A, B, error = validate_numbers(data)
        if error:
            return error
        if B == 0:
            return JsonResponse({"error": "Division by zero!"}, status=400)
        return JsonResponse({"answer": A / B})
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data."}, status=400)