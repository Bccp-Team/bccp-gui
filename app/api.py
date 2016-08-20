import requests
import json

base_url = "https://ml1"

def list_ns():
    namespace_url = base_url + "/namespace"
    r = requests.get(namespace_url, verify=False)
    res = r.json()
    if not res: res = []
    return res

def list_batchs(active=False, limit=0,offset=0):
    batchs_url = base_url + "/batch"
    if active: batchs_url += "/active"
    r = requests.get(batchs_url, verify=False, data=json.dumps({"limit": limit, "offset":offset}))
    res = r.json()
    if not res: res = []
    return res

def list_repos(namespace):
    repos_url = base_url + "/namespace/" + namespace
    r = requests.get(repos_url, verify=False)
    res = r.json()
    if not res: res = []
    return res

def list_runners(status=None,limit=0,offset=0):
    repos_url = base_url + "/runner"
    data = {'limit': limit, 'offset': offset}
    if status: data['status'] = status
    r = requests.get(repos_url, verify=False, data=json.dumps(data))
    res = r.json()
    if not res: res = []
    return res

def stats_runners():
    repos_url = base_url + "/runner/stats"
    r = requests.get(repos_url, verify=False)
    return r.json()

def stats_run(data={}):
    repos_url = base_url + "/run/stats"
    r = requests.get(repos_url, verify=False, data=json.dumps(data))
    return r.json()

def list_runs(data={}, limit=0, offset=0):
    run_url = base_url + "/run"
    data = dict(data)
    data['limit'] = limit
    data['offset'] = offset
    r = requests.get(run_url, verify=False, data=json.dumps(data))
    res = r.json()
    if not res: res = []
    return res

def get_repo_run(repo_id, limit=0, offset=0):
    return list_runs(data={'repo': str(repo_id)}, limit=limit, offset=offset)

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

def get_runner_run(runner_id, limit=0, offset=0):
    return list_runs(data={'runner': str(runner_id)}, limit=limit, offset=offset)

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

def add_batch(batch):
    runner_url = base_url + "/run"
    r = requests.put(runner_url, verify=False, data=json.dumps(batch))
