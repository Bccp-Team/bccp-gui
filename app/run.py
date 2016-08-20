from flask import render_template
from flask import redirect
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

@app.route('/runs/<int:run_id>/retry')
def retry(run_id):
    run = api.get_run(run_id)
    run = api.add_run_batch(run['batch'], run['repo'])
    return redirect('/runs/' + run['ok'])

@app.route('/runs/<int:run_id>/cancel')
def cancel(run_id):
    api.cancel_run(run_id)
    return redirect('/runs')
