from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/birthday_page', methods=["GET"])
def birthday_page():
    
    return render_template('birthday_page.html')

if __name__ == '__main__':
    app.run(debug=True)

