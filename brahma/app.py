from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/registration/general_open', methods=['GET'])
def registration_form():
    return redirect("https://forms.gle/EzfjbwNRiUqWaT4y7")

@app.route('/registration/general_school', methods=['GET'])
def school_registration_form():
    return redirect("https://forms.gle/W7RFfGgkXTFNvZeLA")

@app.route('/registration/cricket', methods=['GET'])
def cricket_registration_form():
    return redirect("https://forms.gle/ur8KQA6dTcFN5fx6A")

if __name__ == '__main__':
    app.run(debug=True)
