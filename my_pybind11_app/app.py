from flask import Flask, render_template, request
import example  # This is your pybind11 module

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        a = float(request.form.get("a"))
        b = float(request.form.get("b"))
        operation = request.form.get("operation")

        if operation == "add":
            result = example.add(a, b)
        elif operation == "multiply":
            result = example.multiply(a, b)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
