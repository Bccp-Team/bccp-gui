from flask import render_template
from bccp_gui import app
from bccp_gui import api

@app.route('/')
@app.route('/index')
def index():
    stats_batch = api.stats_batch()
    stats_runners = api.stats_runners()
    stats_run_global = api.stats_run()
    return render_template('index.html', stats_batch = stats_batch,
            stats_runners = stats_runners, stats_run_global = stats_run_global)
