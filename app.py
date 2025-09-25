from flask import Flask, request

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Flask App</title>
  </head>
  <body>
    {content}
  </body>
</html>
""".strip()


@app.route("/")
def home():
    content = "<h1>Welcome to Flask App</h1>"
    return TEMPLATE.format(content=content)


@app.route("/add/<x>/<y>")
def add(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return "Invalid numbers", 400
    result = f"{x} + {y} = {x + y}"
    return TEMPLATE.format(content=f"<p>{result}</p>")



@app.route("/reverse")
def reverse():
    q = request.args.get("q", "")
    reversed_q = q[::-1]
    return TEMPLATE.format(content=f"<p>{q}: {reversed_q}</p>")


if __name__ == "__main__":
    app.run(debug=True)
