from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index_route():
    return render_template('index.html')

@app.route('/project.html')
def project():
    return render_template('project.html')

@app.route('/about.html')
def about():
    return render_template('about.html')
