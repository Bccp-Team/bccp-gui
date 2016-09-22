from flask import render_template
from flask import redirect
from app import app
from app import api

@app.route('/runs')
@app.route('/runs/<kind>/<int:offset>')
def runs(kind="waiting",offset = 0):
    if kind == 'all':
        runs = api.list_runs(limit = 10, offset = offset)
    else:
        runs = api.list_runs(data={'status':kind}, limit = 10, offset = offset)
    stats_runners = api.stats_runners()
    stats_run = api.stats_run()
    stats_batch = api.stats_batch()
    return render_template('runs.html', runs = runs, kind = kind, stats_runners =
        stats_runners, stats_run = stats_run, stats_batch = stats_batch, offset = offset)

@app.route('/runs/<int:run_id>')
def run(run_id):
    run = api.get_run(run_id)
    stats_runners = api.stats_runners()
    stats_run = api.stats_run()
    stats_batch = api.stats_batch()
    return render_template('run.html', run = run, stats_runners =
        stats_runners, stats_run = stats_run, stats_batch = stats_batch)

@app.route('/runs/<int:run_id>/retry')
def retry(run_id):
    run = api.get_run(run_id)
    run = api.add_run_batch(run)
    return redirect('/runs/' + str(run.id))

@app.route('/runs/<int:run_id>/cancel')
def cancel(run_id):
    api.cancel_run(api.get_run(run_id))
    return redirect('/runs')
