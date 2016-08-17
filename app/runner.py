from flask import render_template
from app import app
from app import api

@app.route('/runners')
def runners():
    runners = api.list_runners()
    return render_template('runners.html', runners=runners)

@app.route('/runners/<int:runner_id>')
def runner(runner_id):
    runner = api.get_runner(runner_id)
    runs = api.get_runner_run(runner_id)
    return render_template('runner.html', runner=runner, runs=runs)
