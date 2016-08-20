from flask import render_template
from flask import redirect
from app import app
from app import api

@app.route('/runners')
@app.route('/runners/<kind>/<int:offset>')
def runners(kind='waiting', offset=0):
    data = {}
    status = None
    if kind != 'all':
        status = kind
    runners = api.list_runners(status=status, offset=offset, limit=10)
    stats = api.stats_runners()
    return render_template('runners.html', runners=runners, stats=stats, offset=offset, kind=kind)

@app.route('/runners/<int:runner_id>')
def runner(runner_id):
    runner = api.get_runner(runner_id)
    runs = api.get_runner_run(runner_id)
    return render_template('runner.html', runner=runner, runs=runs)

@app.route('/runners/<int:runner_id>/kill')
def kill(runner_id):
    api.kill_runner(runner_id)
    return redirect('/runners')
