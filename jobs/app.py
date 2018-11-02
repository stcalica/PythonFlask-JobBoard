import flask, render_templates from Flask

app = Flask(__name__)


@app.route('/jobs')
def jobs():
    return render_templates('index.html')
