from flask import render_template
from flask import redirect
from flask import request
from bccp_gui import app
from bccp_gui import api

@app.route('/runs/')
@app.route('/runs/<kind>')
@app.route('/runs/<kind>/<int:offset>/<int:limit>')
@app.route('/runs/<int:offset>/<int:limit>')
def runs(kind="waiting", offset=0, limit=2000):
    if kind == 'all':
        runs = api.list_runs(offset=offset, limit=limit)
    else:
        runs = api.list_runs(data={'status':kind})
    stats_runners = api.stats_runners()
    stats_run_global = api.stats_run()
    stats_batch = api.stats_batch()
    return render_template('runs.html', runs = runs, kind = kind, stats_runners =
        stats_runners, stats_run_global = stats_run_global, stats =
        stats_run_global, stats_batch = stats_batch)

@app.route('/runs/<int:run_id>')
@app.route('/runs/<int:run_id>')
def run(run_id):
    run = api.get_run(run_id)
    stats_runners = api.stats_runners()
    stats_run_global = api.stats_run()
    stats_batch = api.stats_batch()
    return render_template('run.html', run = run, stats_runners =
        stats_runners, stats_run_global = stats_run_global, stats_batch =
        stats_batch)

@app.route('/runs/<int:run_id>/retry')
def retry(run_id):
    run = api.get_run(run_id)
    run = api.add_run_batch(run)
    return redirect('/runs/' + str(run.id))

@app.route('/runs/<int:run_id>/cancel')
def cancel(run_id):
    api.cancel_run(api.get_run(run_id))
    return redirect('/runs')

@app.route('/runs/search', methods = ['POST'])
def runs_search():
    return redirect('/runs/' + request.form['id'] + "/20")
