from flask import render_template
from app import app
from app import api

@app.route('/batchs')
def batchs():
    batchs = api.list_batchs()
    return render_template('batchs.html', batchs=batchs)

@app.route('/batchs/<int:batch_id>')
def batch(batch_id):
    batch = api.get_batch(batch_id)
    return render_template('batch.html', batch=batch, runs=batch['runs'])
