import requests
import json
import bccp_gui.api_pb2.api_pb2 as api_pb2
import grpc
import bccp_gui


stub = None

def start_api(srv):
    global stub
    channel = grpc.insecure_channel(srv)
    stub = api_pb2.ApiStub(channel)

def list_ns():
    return stub.NamespaceList(api_pb2.Criteria())

def list_batchs(active=False, limit=0,offset=0):
    if active:
        return stub.BatchListActive(api_pb2.Criteria(filters={}, limit=limit, offset=offset))
    else:
        return stub.BatchList(api_pb2.Criteria(filters={}, limit=limit, offset=offset))

def list_repos(namespace):
    return stub.NamespaceGet(api_pb2.Namespace(name=namespace))

def list_runners(status=None,limit=0,offset=0):
    if status:
        return stub.RunnerList(api_pb2.Criteria(filters={"status": status}, limit=0, offset=0))
    else:
        return stub.RunnerList(api_pb2.Criteria(limit=0, offset=0))

def stats_runners():
    return stub.RunnerStat(api_pb2.Criteria())

def stats_run(data={}):
    return stub.RunStat(api_pb2.Criteria(filters=data))

def stats_batch(data={}):
    return stub.BatchStat(api_pb2.Criteria(filters=data))

def list_runs(data={}, limit=0, offset=0):
    return stub.RunList(api_pb2.Criteria(filters=data, limit=limit, offset=offset))

def get_repo_run(repo_id, limit=0, offset=0):
    return list_runs(data={'repo': str(repo_id)}, limit=limit, offset=offset)

def get_batch(batch_id):
    return stub.BatchGet(api_pb2.Batch(id=batch_id))

def get_run(run_id):
    return stub.RunGet(api_pb2.Run(id=run_id))

def get_runner(runner_id):
    return stub.RunnerGet(api_pb2.Runner(id=runner_id))

def get_runner_run(runner_id, limit=0, offset=0):
    return list_runs(data={'runner': str(runner_id)}, limit=limit, offset=offset)

def add_run_batch(run):
    run.priority = 5
    return stub.RunStart(run)

def cancel_run(run):
    return stub.RunCancel(run)

def kill_runner(run):
    return stub.RunnerKill(run)

def add_batch(batch):
    return stub.BatchStart(api_pb2.BatchCreation(batch=batch, priority=2))
