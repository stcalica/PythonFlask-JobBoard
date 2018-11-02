from flask import Flask, render_templates

app = Flask(__name__)


@app.route('/jobs')
def jobs():
    return render_templates('index.html')
