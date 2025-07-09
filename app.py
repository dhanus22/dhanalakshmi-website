from flask import Flask, render_template, request, redirect
from tinydb import TinyDB
from datetime import datetime

app = Flask(__name__)

# Create or open a local JSON database
db = TinyDB('contact_db.json')

# Route: Home Page


# Route: About Us Page
@app.route('/about')
def about():
    return render_template('about.html')

# Route: Services Page
@app.route('/services')
def services():
    return render_template('services.html')

# Route: Contact Us Page with form handling
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        db.insert({
            'name': request.form['name'],
            'email': request.form['email'],
            'message': request.form['message']
        })
    return render_template('index.html')

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow}

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
