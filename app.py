from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template for calculations
HTML_TEMPLATE = """
<!doctype html>
<html>
    <head>
        <title>Simple Calculator</title>
    </head>
    <body>
        <h1>Simple Calculator</h1>
        <form method="POST">
            <label for="num1">Enter first number:</label>
            <input type="number" id="num1" name="num1" required>
            <br><br>
            <label for="num2">Enter second number:</label>
            <input type="number" id="num2" name="num2" required>
            <br><br>
            <label for="operation">Select an operation:</label>
            <select id="operation" name="operation">
                <option value="add">Addition</option>
                <option value="subtract">Subtraction</option>
                <option value="multiply">Multiplication</option>
                <option value="divide">Division</option>
            </select>
            <br><br>
            <button type="submit">Calculate</button>
        </form>

        {% if result is not none %}
            <h2>Result:</h2>
            <p>{{ result }}</p>
        {% endif %}

        {% if error %}
            <h2>Error:</h2>
            <p>{{ error }}</p>
        {% endif %}
    </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None

    if request.method == "POST":
        try:
            # Retrieve inputs
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operation = request.form.get("operation")

            # Perform calculation
            if operation == "add":
                result = f"The sum is: {num1 + num2}"
            elif operation == "subtract":
                result = f"The difference is: {num1 - num2}"
            elif operation == "multiply":
                result = f"The product is: {num1 * num2}"
            elif operation == "divide":
                if num2 != 0:
                    result = f"The quotient is: {num1 / num2}"
                else:
                    error = "Division by zero is not allowed."
            else:
                error = "Invalid operation selected."
        except ValueError:
            error = "Invalid number(s) entered."

    return render_template_string(HTML_TEMPLATE, result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
