from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

def calc_opr(request):
    result = None
    num1 = num2 = ''
    operation = '+'

    if request.method == 'POST':
        num1 = request.POST.get('num1', '')
        num2 = request.POST.get('num2', '')
        operation = request.POST.get('operation', '+')

        try:
            num1_float = float(num1)
            num2_float = float(num2)
            if operation == '+':
                result = num1_float + num2_float
            elif operation == '-':
                result = num1_float - num2_float
            elif operation == '*':
                result = num1_float * num2_float
            elif operation == '/':
                result = num1_float / num2_float
        except Exception as e:
            result = f"Error: {e}"

    return render(request, 'calc_pages/index.html', {
        'result': result,
        'num1': num1,
        'num2': num2,
        'operation': operation
    })
