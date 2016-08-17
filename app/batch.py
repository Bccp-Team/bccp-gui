from flask import render_template
from app import app
from app import api

@app.route('/batchs')
def batchs():
    batchs = api.list_batchs()
    return render_template('batchs.html', batchs=batchs)

@app.route('/batchs/<int:batch_id>')
@app.route('/batchs/<int:batch_id>/<kind>')
def batch(batch_id, kind = 'waiting'):
    batch = api.get_batch(batch_id)
    for key in batch['runs']:
        if batch['runs'][key] == None: batch['runs'][key] = []
    return render_template('batch.html', batch=batch, runs=batch['runs'], kind=kind)
