from flask import render_template
from flask import redirect
from flask import request
from app import app
from app import api

@app.route('/namespaces')
def namespaces():
    namespaces = api.list_ns()
    print(namespaces)
    stats_batch = api.stats_batch()
    stats_runners = api.stats_runners()
    stats_run_global = api.stats_run()
    return render_template('namespaces.html', namespaces = namespaces, stats_runners =
        stats_runners, stats_run_global = stats_run_global, stats_batch = stats_batch)

@app.route('/namespaces/<namespace>')
def namespace(namespace):
    repos = api.list_repos(namespace)
    stats_batch = api.stats_batch()
    stats_runners = api.stats_runners()
    stats_run_global = api.stats_run()
    return render_template('namespace.html', namespace = namespace, repos =
         repos, stats_runners = stats_runners, stats_run_global = stats_run_global,
         stats_batch = stats_batch)

@app.route('/namespaces/repo/<int:repo_id>')
@app.route('/namespaces/repo/<int:repo_id>/<kind>')
@app.route('/namespaces/repo/<int:repo_id>/<kind>')
def repo(repo_id, kind="running"):
    if kind == 'all':
        runs = api.list_runs(data = {'repo':str(repo_id)})
    else:
        runs = api.list_runs(data = {'status':kind, 'repo':str(repo_id)})
    stats = api.stats_run(data = {'repo':str(repo_id)})
    if not runs: runs = []
    stats_batch = api.stats_batch()
    stats_runners = api.stats_runners()
    stats_run_global = api.stats_run()
    return render_template('repo.html', repo = repo_id, runs = runs, kind =
        kind, stats = stats, stats_runners =
        stats_runners, stats_run_global = stats_run_global, stats_batch = stats_batch)

@app.route('/namespaces/search', methods = ['POST'])
def namespaces_search():
    return redirect('/namespaces/' + request.form['id'])
