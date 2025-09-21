from flask import Flask
app=Flask(__name__)
@app.route("/")
def sayhello():
    return "hello,world"

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
    git remote add origin https://github.com/MRSE435/Flask-Development-.git
