from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

def calc_opr(request):
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            operation = request.POST.get("operation")

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
            else:
                result = "Invalid operation"
        except Exception as e:
            result = f"Error: {str(e)}"

    return render(request, "calc_pages/index.html", {"result": result})
