from flask import render_template
from app import app
from app import api

@app.route('/namespaces')
def namespaces():
    namespaces = api.list_ns()
    print(namespaces)
    return render_template('namespaces.html', namespaces=namespaces)

@app.route('/namespaces/<namespace>')
def namespace(namespace):
    repos = api.list_repos(namespace)
    return render_template('namespace.html', namespace=namespace, repos=repos)

@app.route('/namespaces/repo/<int:repo_id>')
@app.route('/namespaces/repo/<int:repo_id>/<kind>/<int:offset>')
def repo(repo_id, kind="running", offset=0):
    if kind == 'all':
        runs = api.list_runs(data={'repo':str(repo_id)}, limit = 10, offset=offset)
    else:
        runs = api.list_runs(data={'status':kind, 'repo':str(repo_id)}, limit = 10, offset=offset)
    stats = api.stats_run(data={'repo':str(repo_id)})
    if not runs: runs = []
    return render_template('repo.html', repo=repo_id, runs=runs, kind=kind, stats=stats, offset=offset)
