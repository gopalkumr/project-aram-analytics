from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Hello, World! This is my cloud-deployed web app.</h1>
        <button onclick="window.location.href='/calculator'">Go to Calculator</button>
    '''

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operator = request.form.get('operator')

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                return "Invalid operator."

            return f"The result of {num1} {operator} {num2} is {result}."
        except ValueError:
            return "Please enter valid numbers."
    return '''
        <form method="post">
            Number 1: <input type="text" name="num1"><br>
            Number 2: <input type="text" name="num2"><br>
            Operator: <input type="text" name="operator"><br>
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)