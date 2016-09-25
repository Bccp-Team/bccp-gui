from flask import render_template
from flask import redirect
from flask import request
from app import app
from app import api

@app.route('/runners')
@app.route('/runners/<kind>')
def runners(kind = 'waiting'):
    data = {}
    status = None
    if kind != 'all':
        status = kind
    runners = api.list_runners(status = status)
    stats_runners = api.stats_runners()
    stats_run_global = api.stats_run()
    stats_batch = api.stats_batch()
    return render_template('runners.html', runners = runners, stats_runners =
        stats_runners, stats_run_global = stats_run_global, stats_batch = stats_batch,
        kind = kind)

@app.route('/runners/<int:runner_id>')
@app.route('/runners/<int:runner_id>/<kind>')
def runner(runner_id, kind = 'running'):
    if kind == 'all':
        runs = api.list_runs(data = {'runner': str(runner_id)})
    else:
        runs = api.list_runs(data = {'runner': str(runner_id),'status':kind})
    runner = api.get_runner(runner_id)
    stats = api.stats_run(data = {'runner':str(runner_id)})
    stats_runners = api.stats_runners()
    stats_run_global = api.stats_run()
    stats_batch = api.stats_batch()
    return render_template('runner.html', runner = runner, runs = runs,
        stats_runners = stats_runners, stats_run_global = stats_run_global,
        stats_batch = stats_batch, stats = stats, kind = kind)

@app.route('/runners/<int:runner_id>/kill')
def kill(runner_id):
    api.kill_runner(api.get_runner(runner_id))
    return redirect('/runners')

@app.route('/runners/search', methods = ['POST'])
def runners_search():
    return redirect('/runners/' + request.form['id'])
