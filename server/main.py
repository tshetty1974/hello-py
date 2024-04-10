from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return print("hello, laya!")
#some changes
#hello
#gsdiug
if __name__ == "__main__":
    app.run(debug=True)
