from flask import Flask, render_template, request , url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    name = None
    email = None
    if request.method == 'POST':
      name = request.form.get('name').lower()
      email = request.form.get('email')
      with open('data.txt' , 'a') as file:
        file.write(f"Name:{name}   Email:{email}  /  ")
    return render_template('index.html', name = name, email = email)
    

app.run(host='0.0.0.0', port=81)   