from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """ <!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/example.html" method="POST">
            <label for="rot"><strong>Rotate by: </strong></label>
            <input type="text" name="rot" id="rot" value="0">
            <textarea id="" name="text"></textarea>
            <input type="submit" value="Submit Query">
        </form>
    </body>
</html> """

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt(text, rot):
    message = ""
    for pos in range(len(text)):
        message += rotate_string(text, rot)
    return message
    


    app.run()