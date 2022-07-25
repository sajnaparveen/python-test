from flask import Flask
app = Flask(__name__)
@app.route('/')
def hellow():
    return "hellow"
if __name__ == "--main__":
    app.run(debug=True)