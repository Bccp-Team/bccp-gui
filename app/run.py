from flask import render_template
from app import app
from app import api

@app.route('/runs')
def runs():
    runs = api.list_runs()
    return render_template('runs.html', runs=runs)

@app.route('/runs/<int:run_id>')
def run(run_id):
    run = api.get_run(run_id)
    return render_template('run.html', run=run)
