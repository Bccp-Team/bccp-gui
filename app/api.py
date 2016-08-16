import requests
import json

base_url = "https://ml1"

def list_ns():
    namespace_url = base_url + "/namespace"
    r = requests.get(namespace_url, verify=False)
    return r.json()

def list_batchs():
    batchs_url = base_url + "/batch"
    r = requests.get(batchs_url, verify=False, data=json.dumps({}))
    return r.json()

def list_repos(namespace):
    repos_url = base_url + "/namespace/" + namespace
    r = requests.get(repos_url, verify=False)
    return r.json()

def get_repo_run(repo_id):
    run_url = base_url + "/run"
    r = requests.get(run_url, verify=False, data=json.dumps({'repo': str(repo_id)}))
    return r.json()

def get_batch(batch_id):
    batch_url = base_url + "/batch/" + str(batch_id)
    r = requests.get(batch_url, verify=False)
    return r.json()
