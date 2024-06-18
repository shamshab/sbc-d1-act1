from flask import Flask

app = Flask[__name__]
app.config["SECRET_KEY"] = ""


@app.route("/")
def index():
    return "Hello, world!"

app.run()