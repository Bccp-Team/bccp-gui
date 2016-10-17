from flask import render_template
from flask import redirect
from flask import request
from bccp_gui import app
from bccp_gui import api

@app.route('/batchs')
@app.route('/batchs/<kind>')
def batchs(kind="active"):
    if kind == "active":
        batchs = api.list_batchs(active = True)
    else:
        batchs = api.list_batchs()
    stats_batch = api.stats_batch()
    stats_runners = api.stats_runners()
    stats_run_global = api.stats_run()
    return render_template('batchs.html', batchs = batchs, kind = kind,
          stats_batch = stats_batch, stats_runners =
          stats_runners, stats_run_global = stats_run_global)

@app.route('/batchs/<int:batch_id>')
@app.route('/batchs/<int:batch_id>/<kind>')
def batch(batch_id, kind = 'waiting'):
    if kind == 'all':
        runs = api.list_runs(data = {'batch':str(batch_id)})
    else:
        runs = api.list_runs(data = {'status':kind, 'batch':str(batch_id)})
    stats = api.stats_run(data = {'batch':str(batch_id)})
    stats_batch = api.stats_batch()
    stats_runners = api.stats_runners()
    stats_run_global = api.stats_run()
    batch = api.get_batch(batch_id)
    print(batch)
    return render_template('batch.html', batch = batch, runs = runs, kind =
        kind, stats_batch = stats_batch, stats_runners =
        stats_runners, stats_run_global = stats_run_global, stats = stats)

@app.route('/batchs/<int:batch_id>/restart')
def restart(batch_id):
    batch = api.get_batch(batch_id)
    api.add_batch(batch)
    return redirect('/batchs')

@app.route('/batchs/search', methods = ['POST'])
def batchs_search():
    return redirect('/batchs/' + request.form['id'])
