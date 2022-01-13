from flask import Flask

app = Flask(__name__)

print("Start of file")
@app.route("/")
def hello_world():
    return "Hello, Docker!"
app.run(host="0.0.0.0", port=8000, debug=True)
print("EOF")
