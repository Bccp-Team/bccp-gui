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
@app.route('/runners/<int:runner_id>/<kind>/<int:offset>')
def runner(runner_id, offset=0, kind='running'):
    if kind == 'all':
        runs = api.list_runs(data={'runner': str(runner_id)}, limit=10, offset=offset)
    else:
        runs = api.list_runs(data={'runner': str(runner_id),'status':kind}, limit=10, offset=offset)
    runner = api.get_runner(runner_id)
    stats = api.stats_run(data={'runner':str(runner_id)})
    return render_template('runner.html', runner=runner, runs=runs, stats=stats, kind=kind, offset=offset)

@app.route('/runners/<int:runner_id>/kill')
def kill(runner_id):
    api.kill_runner(runner_id)
    return redirect('/runners')
