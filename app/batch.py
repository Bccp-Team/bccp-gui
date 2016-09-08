from flask import render_template
from flask import redirect
from app import app
from app import api

@app.route('/batchs')
@app.route('/batchs/<kind>/<int:offset>')
def batchs(kind="active", offset=0):
    if kind == "active":
        batchs = api.list_batchs(active=True, offset=offset, limit=10)
    else:
        batchs = api.list_batchs(offset=offset, limit=10)
    stats = api.stats_batch()
    return render_template('batchs.html', batchs=batchs, kind=kind, stats=stats, offset=offset)

@app.route('/batchs/<int:batch_id>')
@app.route('/batchs/<int:batch_id>/<kind>/<int:offset>')
def batch(batch_id, offset=0, kind = 'waiting'):
    if kind == 'all':
        runs = api.list_runs(data={'batch':str(batch_id)}, limit = 10, offset=offset)
    else:
        runs = api.list_runs(data={'status':kind, 'batch':str(batch_id)}, limit = 10, offset=offset)
    stats = api.stats_run(data={'batch':str(batch_id)})
    batch = api.get_batch(batch_id)
    print(batch)
    return render_template('batch.html', batch=batch, runs=runs, kind=kind, stats=stats, offset=offset)

@app.route('/batchs/<int:batch_id>/restart')
def restart(batch_id):
    batch = api.get_batch(batch_id)
    api.add_batch(batch)
    return redirect('/batchs')
