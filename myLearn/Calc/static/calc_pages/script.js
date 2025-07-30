document.addEventListener("DOMContentLoaded", function () {
    const calcBtn = document.getElementById("calc-btn");
    const clearBtn = document.getElementById("clear-btn");
    const form = document.getElementById("calc-form");
    const resultLabel = document.getElementById("result-label");

    calcBtn.addEventListener("click", function (e) {
        e.preventDefault();
        calculate();
    });

    clearBtn.addEventListener("click", function (e) {
        e.preventDefault();
        form.reset();
        resultLabel.value = "";
    });

    function calculate() {
        const num1El = document.getElementById("num1");
        const num2El = document.getElementById("num2");
        const operationEl = document.getElementById("operation");

        if (!num1El || !num2El || !operationEl) {
            alert("Some input fields are missing!");
            return;
        }

        const num1 = parseFloat(num1El.value);
        const num2 = parseFloat(num2El.value);
        const operation = operationEl.value;

        let result;
        if (isNaN(num1) || isNaN(num2)) {
            result = "Please enter valid numbers.";
        } else {
            switch (operation) {
                case '+':
                    result = num1 + num2;
                    break;
                case '-':
                    result = num1 - num2;
                    break;
                case '*':
                    result = num1 * num2;
                    break;
                case '/':
                    result = num2 !== 0 ? (num1 / num2).toFixed(2) : "Cannot divide by zero";
                    break;
                default:
                    result = "Invalid operation";
            }
        }

        resultLabel.value = "Result: " + result;
    }
});
