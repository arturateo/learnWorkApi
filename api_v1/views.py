import json
from django.http import JsonResponse


def json_add_view(request, *args, **kwargs):
    try:
        body = json.loads(request.body)
        add = int(body['A']) + int(body['B'])
        answer = {
            'answer': add
        }
        return JsonResponse(answer)
    except ValueError:
        response = JsonResponse({'error': 'Ошибка сложения! Одно из чисел является текстом'})
        response.status_code = 400
        return response


def json_subtract_view(request, *args, **kwargs):
    try:
        body = json.loads(request.body)
        subtract = int(body['A']) - int(body['B'])

        answer = {
            'answer': subtract
        }
        return JsonResponse(answer)
    except ValueError:
        response = JsonResponse({'error': 'Ошибка вычитания! Одно из чисел является текстом'})
        response.status_code = 400
        return response


def json_multiply_view(request, *args, **kwargs):
    try:
        body = json.loads(request.body)
        multiply = int(body['A']) * int(body['B'])
        answer = {
            'answer': multiply
        }
        return JsonResponse(answer)
    except ValueError:
        response = JsonResponse({'error': 'Ошибка умножения! Одно из чисел является текстом'})
        response.status_code = 400
        return response


def json_divide_view(request, *args, **kwargs):
    try:
        body = json.loads(request.body)
        divide = int(body['A']) / int(body['B'])
        answer = {
            'answer': divide
        }
        return JsonResponse(answer)
    except ValueError:
        response = JsonResponse({'error': 'Ошибка деления! Одно из чисел является текстом.'})
        response.status_code = 400
        return response
    except ZeroDivisionError:
        response = JsonResponse({'error': 'Ошибка деления! Одно из чисел является нулем. На ноль делить нельзя!'})
        response.status_code = 400
        return response
