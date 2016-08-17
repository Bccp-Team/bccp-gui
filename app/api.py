import requests
import json

base_url = "https://ml1"

def list_ns():
    namespace_url = base_url + "/namespace"
    r = requests.get(namespace_url, verify=False)
    res = r.json()
    if not res: res = []
    return res

def list_batchs():
    batchs_url = base_url + "/batch"
    r = requests.get(batchs_url, verify=False, data=json.dumps({}))
    res = r.json()
    if not res: res = []
    return res

def list_repos(namespace):
    repos_url = base_url + "/namespace/" + namespace
    r = requests.get(repos_url, verify=False)
    res = r.json()
    if not res: res = []
    return res

def list_runners():
    repos_url = base_url + "/runner"
    r = requests.get(repos_url, verify=False, data=json.dumps({}))
    res = r.json()
    if not res: res = []
    return res

def list_runs(status = None):
    run_url = base_url + "/run"
    if status:
        r = requests.get(run_url, verify=False, data=json.dumps({'status': status}))
    else:
        r = requests.get(run_url, verify=False, data=json.dumps({}))
    res = r.json()
    if not res: res = []
    return res

def get_repo_run(repo_id):
    run_url = base_url + "/run"
    r = requests.get(run_url, verify=False, data=json.dumps({'repo': str(repo_id)}))
    res = r.json()
    if not res: res = []
    return res

def get_batch(batch_id):
    batch_url = base_url + "/batch/" + str(batch_id)
    r = requests.get(batch_url, verify=False)
    return r.json()

def get_run(run_id):
    run_url = base_url + "/run/" + str(run_id)
    r = requests.get(run_url, verify=False)
    return r.json()

def get_runner(runner_id):
    runner_url = base_url + "/runner/" + str(runner_id)
    r = requests.get(runner_url, verify=False)
    return r.json()

def get_runner_run(runner_id):
    run_url = base_url + "/run"
    r = requests.get(run_url, verify=False, data=json.dumps({'runner': str(runner_id)}))
    res = r.json()
    if not res: res = []
    return res

def add_run_batch(batch_id, repo_id):
    run_url = base_url + "/run/%d/%d" % (batch_id, repo_id)
    print(run_url)
    r = requests.put(run_url, verify=False)
    return r.json()

def cancel_run(run_id):
    run_url = base_url + "/run/" + str(run_id)
    r = requests.delete(run_url, verify=False)
    return r.json()

def kill_runner(run_id):
    runner_url = base_url + "/runner/" + str(run_id)
    r = requests.delete(runner_url, verify=False)
    return r.json()
