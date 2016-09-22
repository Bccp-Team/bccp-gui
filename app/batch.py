from flask import render_template
from flask import redirect
from app import app
from app import api

@app.route('/batchs')
@app.route('/batchs/<kind>/<int:offset>/<int:per_page>')
def batchs(kind="active", offset = 0, per_page = 20):
    if kind == "active":
        batchs = api.list_batchs(active = True, offset = offset, limit = per_page)
    else:
        batchs = api.list_batchs(offset = offset, limit = per_page)
    stats_batch = api.stats_batch()
    stats_runners = api.stats_runners()
    stats_run = api.stats_run()
    return render_template('batchs.html', batchs = batchs, kind = kind,
          stats_batch = stats_batch, stats_runners =
          stats_runners, stats_run = stats_run, offset = offset, per_page = per_page)

@app.route('/batchs/<int:batch_id>')
@app.route('/batchs/<int:batch_id>/<kind>/<int:offset>/<int:per_page>')
def batch(batch_id, offset = 0, kind = 'waiting', per_page = 20):
    if kind == 'all':
        runs = api.list_runs(data = {'batch':str(batch_id)}, limit = per_page, offset = offset)
    else:
        runs = api.list_runs(data = {'status':kind, 'batch':str(batch_id)}, limit = per_page, offset = offset)
    stats_batch = api.stats_run(data = {'batch':str(batch_id)})
    batch = api.get_batch(batch_id)
    print(batch)
    return render_template('batch.html', batch = batch, runs = runs, kind =
        kind, stats_batch = stats_batch, stats_runners =
        stats_runners, stats_run = stats_run,offset = offset, per_page = per_page)

@app.route('/batchs/<int:batch_id>/restart')
def restart(batch_id):
    batch = api.get_batch(batch_id)
    api.add_batch(batch)
    return redirect('/batchs')
