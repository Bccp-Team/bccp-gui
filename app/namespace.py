from flask import render_template
from app import app
from app import api

@app.route('/namespaces')
def namespaces():
    namespaces = api.list_ns()
    return render_template('namespaces.html', namespaces=namespaces)

@app.route('/namespaces/<namespace>')
def namespace(namespace):
    repos = api.list_repos(namespace)
    return render_template('namespace.html', namespace=namespace, repos=repos)

@app.route('/namespaces/repo/<int:repo_id>')
def repo(repo_id):
    runs = api.get_repo_run(repo_id)
    if not runs: runs = []
    return render_template('repo.html', runs=runs)
